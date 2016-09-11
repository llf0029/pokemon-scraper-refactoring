"""
@author: Angus Whitehead
"""


class StatisticCalculator:

    def get_min_weight(self, pokedex):
        return self.calculate_min(self.get_pokemon_weights(pokedex))

    def get_max_weight(self, pokedex):
        return self.calculate_max(self.get_pokemon_weights(pokedex))

    def get_avg_weight(self, pokedex):
        return self.calculate_avg(self.get_pokemon_weights(pokedex))

    def get_min_height(self, pokedex):
        return self.calculate_min(self.get_pokemon_heights(pokedex))

    def get_max_height(self, pokedex):
        return self.calculate_max(self.get_pokemon_heights(pokedex))
        
    def get_avg_height(self, pokedex):
        return self.calculate_avg(self.get_pokemon_heights(pokedex))

    # Generates a dictionary of pokemon and their weights
    def get_pokemon_weights(self, pokedex):
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_weight()
        return items

    # Generates a dictionary of pokemon and their heights
    def get_pokemon_heights(self, pokedex):
        items = {}
        for key in pokedex:
            items[key] = pokedex[key].get_height()
        return items

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
    def calculate_avg(self, items):
        num_of_values = len(items)
        sum_of_values = sum(items.values())
        return sum_of_values / num_of_values