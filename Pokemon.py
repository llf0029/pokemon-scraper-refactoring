"""
@author: Angus Whitehead
"""


class Pokemon:
    """
        This class is holding the information about each species
    """

    def __init__(self, pokemon_information, date_added):
        self.name = pokemon_information['name']
        self._index = pokemon_information['number']
        self._image = pokemon_information['image']
        self._type = pokemon_information['type']
        self._desc = pokemon_information['desc']
        self._height = pokemon_information['height']
        self._weight = pokemon_information['weight']
        self._date_added = date_added

    def get_index(self):
        return self._index

    def get_image(self):
        return self._image

    def get_type(self):
        return self._type

    def get_desc(self):
        return self._desc

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_date_added(self):
        return self._date_added
