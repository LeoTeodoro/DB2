import threading
import random
import time
from pymongo import MongoClient

# Instanciando o banco de dados
client = MongoClient("mongodb://localhost:27017")
db = client["bancoiot"]
sensores = db.sensores

# Lista para manter o estado dos sensores
sensores_ativos = [True, True, True]


# Adicionando sensores
def add_sensor(sensor_id):
    new_doc = {
        "sensor_id": sensor_id,
        "ValorSensor": 0,
        "unidadeMedida": "°C",
        "sensorAlarmado": False,
    }
    result = db.sensores.insert_one(new_doc)
    if result.acknowledged:
        print("Sensor adicionado")
    else:
        print("Erro na inserção...")


for i in range(3):
    add_sensor(i + 1)


# Atualizando o valor do sensor
def update_sensor_temp(sensor_id, valor):
    result = db.sensores.update_one(
        {"sensor_id": sensor_id},
        {"$set": {"ValorSensor": valor}},
    )
    # Verifica se o documento foi atualizado
    if result.acknowledged:
        print(str(sensor_id) + " atualizado")
    else:
        print("Erro na atualização...")


# Atualizando o estado do sensor
def update_sensor_alarm(sensor_id, valor):
    result = db.sensores.update_one(
        {"sensor_id": sensor_id},
        {"$set": {"sensorAlarmado": valor}},
    )


# Função que simula um sensor de temperatura
def sensor_temperatura(sensor_id):
    while sensores_ativos[sensor_id - 1]:
        temperatura = random.uniform(30, 40)
        print(f"Sensor {sensor_id}: Temperatura = {temperatura:.2f}°C")

        # Verifica se a temperatura está acima do limite
        if temperatura > 38:
            sensores_ativos[sensor_id - 1] = False
            print(f"Atenção! Temperatura muito alta! Verificar sensor {sensor_id}!")
            update_sensor_alarm(sensor_id, True)
            update_sensor_temp(sensor_id, temperatura)
        else:
            update_sensor_temp(sensor_id, temperatura)

        time.sleep(1)


# Criando três threads para simular três sensores de temperatura
for i in range(3):
    t = threading.Thread(target=sensor_temperatura, args=(i + 1,))
    t.daemon = True  # Define as threads como daemon, para que elas parem quando o programa principal terminar
    t.start()

# Aguarda para permitir a execução das threads
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
