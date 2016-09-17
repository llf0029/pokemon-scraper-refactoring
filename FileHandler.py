"""
@author: Angus Whitehead
"""

import shelve


class FileHandler:

    def save(self, pokemon):
        database = shelve.open('pokedexData.db')
        database[pokemon.name] = pokemon
        database.close()

    def load_database(self):
        database = shelve.open('pokedexData.db')
        loaded_pokemon = []
        for key in database:
            loaded_pokemon.append(database[key])
        database.close()
        return loaded_pokemon
