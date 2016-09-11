"""
@author: Angus Whitehead
"""


class StatisticCalculator:
    
    def get_pokemon_weights(self, pokedex):
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_weight()
        return items

    def get_min_weight(self, pokedex):
        return self.calculate_min(self.get_pokemon_weights(pokedex))

    def get_max_weight(self, pokedex):
        return self.calculate_max(self.get_pokemon_weights(pokedex))

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
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_height()
        return self.calculate_max(items)
        
    def get_avg_height(self, pokedex):
        values = []
        for key in pokedex:
            values.append(pokedex[key].get_height())
        return self.calculate_avg(values)
    
    # Extracted from get_min_height / get_min_weight
    def calculate_min(self, items):
        min_key = ""
        min_val = float('inf')
        for key, value in items.items():
            if value < min_val:
                min_key = key
                min_val = value
        return min_key

    # Extracted from get_max_height / get_max_weight
    def calculate_max(self, items):
        max_key = ""
        max_val = 0
        for key, value in items.items():
            if value > max_val:
                max_key = key
                max_val = value
        return max_key

    # Extracted from get_avg_height / get_avg_weight
    def calculate_avg(self, values):
        num_of_values = len(values)
        sum_of_values = sum(values)
        return sum_of_values / num_of_values