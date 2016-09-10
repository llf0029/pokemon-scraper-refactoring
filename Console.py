"""
@author: Angus Whitehead
"""

from cmd import Cmd


class Console (Cmd):
    """
    this is the user interface
    """
    prompt = ""
    intro = """"""
    my_controller = None

    def __init__(self, the_prompt, the_intro, the_controller):
        super(Console, self).__init__()
        self.prompt = the_prompt
        self.intro = the_intro
        self.my_controller = the_controller

    def do_scrape(self, line, url="http://pokemondb.net/pokedex/",
                  gen=1, p_type="Fire"):
        """
        :param url: this is the base website that the program will go to in
                order to find the data it requires (leave it blank to pass in
                 the default)
        :param gen: this is the generation that you wish to search through
                   (leave it blank to pass in the default of 1)
        :param p_type: this is the type of pokemon to search
                       options are Normal, Fire , Fighting, Water ,Flying,
                       Grass, Poison, Electric, Ground, Psychic,
                       Rock , Ice, Bug, Dragon, Ghost. (leave it blank to pass
                       in the default of fire)
        """
        args = line.split(" ")
        if len(args) > 0 and args[0] is not "":
            url = args[0]
        if len(args) > 1 and args[1] is not "":
            gen = args[1]
        if len(args) > 2 and args[2] is not "":
            p_type = args[2]
        
        self.my_controller.get_from_web(url, gen, p_type)

    def do_save(self, name):
        """
        this function saves the instance of the pokemon class
        :param name: this is the name of the pokemon whose instance you wish
                to save
        """
        if name is "":
            print ("please enter a pokemon's name")
            return

        name = name.title()
        self.my_controller.save_data(name)

    def do_load(self, arg):
        """
        this function loads the saved instances of the pokemon class
        """
        try:
            self.my_controller.get_from_save()
        except IOError:
            print("pokemon not in database")

    def do_stats(self, name):
        """
        this function gathers the stored information on a pokemon species
        :param name: this is the name of the pokemon whose information you wish
         to view
        """
        if name is "":
            print("please enter a pokemon's name")
            return

        name = name.title()
        try:
            self.my_controller.get_stats(name)
        except KeyError:
            print("Pokemon " + name + " doesn't exist in the current data")

    def do_max_weight(self, line):
        """
        this function displays the heaviest Pokemon
        """
        self.my_controller.get_max_weight()

    def do_min_weight(self, line):
        """
        this function displays the lightest pokemon
        """
        self.my_controller.get_min_weight()

    def do_average_weight(self, line):
        """
        this function displays the average weight of all pokemon stored
        """
        self.my_controller.get_avg_weight()

    def do_max_height(self, line):
        """
        this function displays the tallest pokemon
        """
        self.my_controller.get_max_height()

    def do_min_height(self, line):
        """
        this function displays the shortest pokemon
        """
        self.my_controller.get_min_height()

    def do_average_height(self, line):
        """
        this function displays the average weight of all pokemon stored
        """
        self.my_controller.get_avg_height()

    def do_exit(self, line):
        """
        this function allows the user to stop the command interpreter
        :return:
        """
        return True
