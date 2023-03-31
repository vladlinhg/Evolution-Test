from creature import Creature
from food import Food
import random


class Dove(Creature):

    def __init__(self, name):
        super().__init__(name)

    def feed(self, food: list):
        super().feed(food)

    def reproduce(self):
        super().reproduce()

    def dead(self):
        super().dead()

class Hawk(Creature):

    def __init__(self, name):
        super().__init__(name)

    def feed(self, food: list):
        super().feed(food)

    def reproduce(self):
        super().reproduce()

    def dead(self):
        super().dead()