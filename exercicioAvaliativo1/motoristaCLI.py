from classes import *


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        notas = 0
        corridas = []
        qntCorridas = int(
            input("Entre com a quantidade corridas que serão cadastradas: ")
        )
        for i in range(qntCorridas):
            nota = int(input("Entre com a nota da corrida: "))
            notas += nota
            distancia = float(input("Entre com a distância da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
            corridas.append(vars(corrida))
        nota = notas / qntCorridas
        motorista = Motorista(corridas, nota)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista(id)
        if motorista:
            print(f"Nota: {motorista['nota']}")
            print("Corridas: ")
            for i in motorista["corridas"]:
                print(f"Nota: {i['nota']}")
                print(f"Distância: {i['distancia']}")
                print(f"Valor: {i['valor']}")
                print(f"Nome do passageiro: {i['passageiro']['nome']}")
                print(f"Documento do passageiro: {i['passageiro']['documento']}")

    def update_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista(id)
        corridas = motorista["corridas"]
        notas = int(motorista["nota"])
        qntCorridas = int(
            input("Entre com a quantidade corridas que serão cadastradas: ")
        )
        for i in range(qntCorridas):
            nota = int(input("Entre com a nota da corrida: "))
            notas += nota
            distancia = float(input("Entre com a distância da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
            corridas.append(vars(corrida))
        notaMedia = notas / (qntCorridas + 1)
        motorista = Motorista(corridas, notaMedia)
        self.motorista_model.update_motorista(motorista, id)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
