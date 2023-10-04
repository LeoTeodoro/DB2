from pymongo import MongoClient
from bson.objectid import ObjectId
from database import Database
from classes import Motorista


class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        try:
            self.db.collection.insert_one(vars(motorista))
            print("Motorista criado com sucesso")
        except:
            print("Erro ao criar motorista")

    def read_motorista(self, idMotorista: str):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(idMotorista)})
            if motorista:
                print(f"Motorista encontrado: {motorista}")
                return motorista
            else:
                print(f"Nenhum motorista encontrado com o id {idMotorista}")
                return None
        except:
            print("Erro ao ler motorista")
            return None

    def update_motorista(self, motorista: Motorista, idMotorista: str):
        try:
            self.db.collection.find_one_and_update(
                {"_id": ObjectId(idMotorista)}, {"$set": vars(motorista)}
            )
            print("Motorista atualizado com sucesso")
        except:
            print("Erro ao atualizar motorista")

    def delete_motorista(self, idMotorista: str):
        try:
            self.db.collection.delete_one({"_id": ObjectId(idMotorista)})
            print("Motorista deletado com sucesso")
        except:
            print("Erro ao deletar motorista")
