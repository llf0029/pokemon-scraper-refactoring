"""
@author: Angus Whitehead
"""


class StatisticCalculator:

    def get_min_weight(self, pokedex):
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_weight()
        return self.calculate_min(items)

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
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_height()
        return self.calculate_min(items)

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
    
    # Extracted from get_min_height / get_min_weight
    def calculate_min(self, items):
        min_val = 1000000000
        min_key = ""
        for key, value in items.items():
            if value < min_val:
                min_val = value
                min_key = key
        return min_key

    # Extracted from get_avg_height / get_avg_weight
    def calculate_avg(self, values):
        num_of_values = len(values)
        sum_of_values = sum(values)
        return sum_of_values / num_of_values