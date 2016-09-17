# Imports
import View

# Abstract base class
class CmdView(View.View):

    def display_message(self, message):
        print (message.encode('ascii', 'replace').decode())

    def error_not_found(self, pokemon_name):
        pass

    def display_added_pokemon(self, pokemon):
        print(species.name + " added")

    def display_pokemon_stats(self, pokemon):
        pass

    def display_weight_min(self, pokemon_name, pokemon_weight):
        pass

    def display_weight_max(self, pokemon_name, pokemon_weight):
        pass

    def display_weight_avg(self, pokemon_name, pokemon_weight):
        pass

    def display_height_min(self, pokemon_name, pokemon_height):
        pass

    def display_height_max(self, pokemon_name, pokemon_height):
        pass

    def display_height_avg(self, pokemon_name, pokemon_height):
        pass
