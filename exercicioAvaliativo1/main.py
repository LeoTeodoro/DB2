from database import Database
from classes import *
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="atlas-cluster", collection="Motoristas")
motoristaModel = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaModel)
motoristaCLI.run()
