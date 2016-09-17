# Imports
import View

# Abstract base class
class CmdView(View.View):

    def display_message(self, message):
        print (message.encode('ascii', 'replace').decode())

    def error_not_found(self, pokemon_name):
        pass

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

    def display_weight_avg(self, pokemon):
        pass

    def display_height_min(self, pokemon):
        pass

    def display_height_max(self, pokemon):
        pass

    def display_height_avg(self, pokemon):
        pass
