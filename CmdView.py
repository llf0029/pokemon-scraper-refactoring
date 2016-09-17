# Imports
import View

# Abstract base class
class CmdView(View.View):

    def display_message(self, message):
        print (message.encode('ascii', 'replace').decode())

    def error_not_found(self, pokemon_name):
        print("pokemon " + pokemon_name + " was not found in the current data")

    def display_added_pokemon(self, pokemon):
        print(pokemon.name + " added")

    def display_pokemon_stats(self, pokemon):
        print(str(pokemon.name))
        print("Nation Number: " + str(pokemon.get_index()))
        print("Image Link: " + pokemon.get_image())
        print("Type: " + pokemon.get_type())
        print("Pokedex Entry: " + pokemon.get_desc())
        print("Height: " + str(pokemon.get_height()) + "m")
        print("Weight: " + str(pokemon.get_weight()) + "kg")

    def display_weight_min(self, pokemon):
        print(
            "the lightest pokemon you have got data on is {} at only {}kg"
            .format(pokemon.name, pokemon.get_weight())
        )

    def display_weight_max(self, pokemon):
        print(
            "the heaviest pokemon you have got data on is {} at a whooping {}kg"
            .format(pokemon.name, pokemon.get_weight())
        )

    def display_weight_avg(self, pokemon_weight):
        print(
            "the average weight of pokemon you have got data on is {}kg"
            .format(pokemon_weight)
        )

    def display_height_min(self, pokemon):
        print(
            "the shortest pokemon you have got data on is {} at only {}m"
            .format(pokemon.name, pokemon.get_height())
        )

    def display_height_max(self, pokemon):
        print(
            "the tallest pokemon you have got data on is {} at a whooping {}m"
            .format(pokemon.name, pokemon.get_height())
        )

    def display_height_avg(self, pokemon_height):
        print(
            "the average height of pokemon you have got data on is {}m"
            .format(pokemon_height)
        )
