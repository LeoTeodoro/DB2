from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db)

pokedex.getAllPokemons()
