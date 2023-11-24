from database import Database
from leagueCRUD import League
from teamCRUD import Team
from cli import TeamCLI

db = Database("bolt://3.234.224.239:7687", "neo4j", "copies-tumble-spacers")
# db.drop_all()

team_db = Team(db)
league_db = League(db)

cli = TeamCLI(team_db)
cli.run()

# Criando liga
league_db.create(
    ["Flamengo", "Palmeiras", "Real Madrid", "Manchester City"], "Mundial de Clubes"
)

# Atualizando uma liga
league_db.update("Mundial de Clubes", "Mundial de Clubes da Fifa")

# Buscando Liga especifica
print("\nTimes da liga: ")
for match in league_db.read("Mundial de Clubes da Fifa"):
    print(match)

# Deletando uma Liga
league_db.delete("Mundial de Clubes da Fifa")

db.close()
