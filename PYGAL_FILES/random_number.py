from random import randint

class Die():
    """Class represents one die for game"""
    def __init__(self, num_sides=6):
        """assumption that die is a cube"""
        self.num_sides = num_sides

    def roll(self):
        """return the value from 1 to the number of cube's walls"""
        return randint(1, self.num_sides)
