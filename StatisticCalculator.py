"""
@author: Angus Whitehead
"""


class StatisticCalculator:

    def get_min_weight(self, pokedex):
        min_weight = 1000000000
        lightest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_weight() < min_weight:
                min_weight = pokedex[name].get_weight()
                lightest_pokemon = name
        return lightest_pokemon

    def get_max_weight(self, pokedex):
        max_weight = -1
        heaviest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_weight() > max_weight:
                max_weight = pokedex[name].get_weight()
                heaviest_pokemon = name
        return heaviest_pokemon

    def get_avg_weight(self, pokedex):
        values = []
        for key in pokedex:
            values.append(pokedex[key].get_weight())
        return self.calculate_avg(values)

    def get_min_height(self, pokedex):
        min_height = 1000000000
        shortest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_height() < min_height:
                min_height = pokedex[name].get_height()
                shortest_pokemon = name
        return shortest_pokemon

    def get_max_height(self, pokedex):
        max_height = -1
        tallest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_height() > max_height:
                max_height = pokedex[name].get_height()
                tallest_pokemon = name
        return tallest_pokemon

    def get_avg_height(self, pokedex):
        values = []
        for key in pokedex:
            values.append(pokedex[key].get_height())
        return self.calculate_avg(values)
    
    # Extracted from get_avg_height / get_avg_weight
    def calculate_avg(self, values):
        num_of_values = len(values)
        sum_of_values = 0
        for value in values:
            sum_of_values += value
        avg = sum_of_values / num_of_values
        return avg