# Imports
from abc import ABCMeta, abstractmethod

# Abstract base class
class View(metaclass=ABCMeta):

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def error_not_found(self, pokemon_name):
        pass

    @abstractmethod
    def display_added_pokemon(self, pokemon):
        pass

    @abstractmethod
    def display_pokemon_stats(self, pokemon):
        pass

    @abstractmethod
    def display_weight_min(self, pokemon):
        pass

    @abstractmethod
    def display_weight_max(self, pokemon):
        pass

    @abstractmethod
    def display_weight_avg(self, pokemon):
        pass

    @abstractmethod
    def display_height_min(self, pokemon):
        pass

    @abstractmethod
    def display_height_max(self, pokemon):
        pass

    @abstractmethod
    def display_height_avg(self, pokemon):
        pass
