import random
from dove import Dove

from food import Food


class Pair:
    def __init__(self):
        self.foods = [Food(), Food()]
        self.creatures = []

    def food_distribute(self):
        if len(self.creatures) == 0:
            return
        elif len(self.creatures) == 1:
            self.creatures[0].feed(self.foods)
        else:
            if isinstance(self.creatures[0], Dove) and isinstance(self.creatures[1], Dove):
                self.creatures[0].feed([self.foods[0]])
                self.creatures[1].feed([self.foods[1]])
            elif isinstance(self.creatures[0], Dove) or isinstance(self.creatures[1], Dove):
                foods = self.foods[0].divide(2)
                self.creatures[0].feed([foods[0]])
                self.creatures[1].feed([foods[1]])
                self.creatures[1].feed([self.foods[1]])
            else:
                return



class Resource:
    def __init__(self, num_pair):
        self.pairs = []
        for i in range(num_pair):
            pair_instance = Pair()
            self.pairs.append(pair_instance)
    

    def assign_food(self, creatures):
        temp_pairs = []
        random.shuffle(self.pairs)
        random.shuffle(creatures)

        for c in creatures:
            p = random.choice(self.pairs)
            p.creatures.append(c)

            if len(p.creatures) == 2:
                self.pairs.remove(p)
                temp_pairs.append(p)
            
        self.pairs += temp_pairs
