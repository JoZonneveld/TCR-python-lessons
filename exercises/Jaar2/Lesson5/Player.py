class Player:

    # constructor
    def __init__(self, name, level):
        self.name = name
        self.level = level

    # getter
    def get_name(self):
        return self.name

    # setter
    def set_name(self, name):
        self.name = name


player = Player('Joost', 20)
