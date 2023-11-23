from database import Database
from leagueCRUD import League
from teamCRUD import Team
from cli import TeamCLI

db = Database("bolt://3.234.224.239:7687", "neo4j", "copies-tumble-spacers")
db.drop_all()

team_db = Team(db)
league_db = League(db)

# cli = TeamCLI(team_db)
# cli.run()

# Criando times
# team_db.create("Flamengo", 1895, 42000000)
# team_db.create("Palmeiras", 1914, 20225600)
# team_db.create("Real Madrid", 1902, 8000000)
# team_db.create("Manchester City", 1894, 30600000)
# team_db.create("Chelsea", 1905, 22000000)

# # Atualizando time
# team_db.update("Flamengo", 42500000)

# # Deletando time
# team_db.delete("Chelsea")

# # Retornando time
# print("Time: ")
# team_db.read("Real Madrid")

# Criando liga
league_db.create(["Flamengo", "Palmeiras", "Real Madrid"], "Mundial de Clubes")

# Atualizando uma liga
league_db.update("Mundial de Clubes", "Mundial de Clubes da Fifa")

# Buscando Liga especifica
print("\nTimes da liga: ")
for match in league_db.read("Mundial de Clubes da Fifa"):
    print(match)

# Deletando uma Liga
league_db.delete("Mundial de Clubes da Fifa")

db.close()
