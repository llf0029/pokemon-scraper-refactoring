"""
@author: Angus Whitehead
"""
import CmdView
import WebScraper
import Pokemon
import Console
import FileHandler
import StatisticCalculator

from datetime import datetime


class Controller:
    pokedex = {}

    def __init__(self):
        self.my_console = Console.Console(
            "(-o-)",
            """Welcome to the personal pokemon encyclopedia (or pokedex for short)
Type help or '?' to see a list of commands""", self)
        self.my_file_handler = FileHandler.FileHandler()
        self.my_Calc = StatisticCalculator.StatisticCalculator()
        self.view = CmdView.CmdView()

    def go(self):
        self.my_console.cmdloop()

    def get_from_web(self, url, gen, p_type):
        my_web = WebScraper.WebScraper(url, gen, p_type)
        p_list = my_web.list_gen()
        for species in p_list:
            pokemon = my_web.info_grab(species)
            self.create_pokemon(species, pokemon)

    def save_data(self, name):
        try:
            pokemon = self.pokedex[name]
            self.my_file_handler.save(pokemon)
            print("pokemon instance saved")
        except KeyError:
            print("pokemon " + name + " was not found in the current data")

    def get_from_save(self):
        p_list = self.my_file_handler.load_database()
        for species in p_list:
            self.pokedex[species.name] = species
            self.view.display_added_pokemon(species)

    def create_pokemon(self, name, pokemon_info):
        pokemon = Pokemon.Pokemon(pokemon_info, datetime.now().ctime())
        self.pokedex[name] = pokemon
        self.view.display_added_pokemon(pokemon)

    def get_stats(self, name):
        self.view.display_pokemon_stats(self.pokedex[name])

    def get_min_weight(self):
        lightest = self.my_Calc.get_min_weight(self.pokedex)
        self.view.display_weight_min(self.pokedex[lightest])

    def get_max_weight(self):
        heaviest = self.my_Calc.get_max_weight(self.pokedex)
        self.view.display_weight_max(self.pokedex[heaviest])

    def get_avg_weight(self):
        avg = self.my_Calc.get_avg_weight(self.pokedex)
        print("the average weight of pokemon you have got data on is " +
              str(avg) + "kg")

    def get_min_height(self):
        shortest = self.my_Calc.get_min_height(self.pokedex)
        height = self.pokedex[shortest].get_height()
        print("the shortest pokemon you have got data on is " + shortest +
              " at only " + str(height) + "m")

    def get_max_height(self):
        tallest = self.my_Calc.get_max_height(self.pokedex)
        height = self.pokedex[tallest].get_height()
        print("the tallest pokemon you have got data on is " + tallest +
              " at a whooping " + str(height) + "m")

    def get_avg_height(self):
        avg = self.my_Calc.get_avg_height(self.pokedex)
        print("the average height of pokemon you have got data on is " +
              str(avg) + "m")
