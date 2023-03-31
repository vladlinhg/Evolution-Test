import random
from food import Food 


class Creature:
    all_creatures = []

    def __init__(self, name):
        self.name = name
        self.food = []
        self.health = 1
        Creature.all_creatures.append(self)
    
    def feed(self, food: list):
        self.food += food
        if Food.sum_values(self.food) > 1:
            self.health = Food.sum_values(self.food)
            self.food = []
            self.reproduce()
        else:
            self.health = Food.sum_values(self.food)
            self.food = []
            self.dead()

    def reproduce(self):
        if random.random() < (self.health - 1):
            return Creature(f'child of {self.name}')
        else:
            return

    
    def dead(self):
        if self.health == 0:
            Creature.all_creatures.remove(self)
        elif self.health < 1:
            if random.random() < (self.health):
                return
            else:
                Creature.all_creatures.remove(self)
        else:
            return
    
    @classmethod
    def get_all_creatures(cls):
        return cls.all_creatures