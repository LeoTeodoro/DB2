from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def getPokemonByName(self, name: str):
        pokemons = self.db.collection.find({"name": name})
        writeAJson(pokemons, "pokemonsName")
        return pokemons

    def getPokemonsByType(self, types: list):
        pokemonsTypes = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemonsTypes, "pokemons_by_type")
        return pokemonsTypes

    def getAllPokemons(self):
        pokemons = self.db.collection.find()
        writeAJson(pokemons, "all_pokemons")
        return pokemons

    def verifyExistingEvolutions(self):
        evolutionPokemons = self.db.collection.find(
            {"next_evolution": {"$exists": True}}
        )
        writeAJson(evolutionPokemons, "evolutions_pokemons")
        return evolutionPokemons

    def getPokemonsMoreThanOneWeakness(self):
        MoreThanOneWeaknessPokemons = self.db.collection.find(
            {"weaknesses": {"$gt": 1}}
        )
        writeAJson(MoreThanOneWeaknessPokemons, "weakness_pokemons")
        return MoreThanOneWeaknessPokemons
