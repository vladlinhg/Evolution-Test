import random

class Food:
    def __init__(self, value=1):
        self.value = float(value)
    

    def divide(self, num):
        return [Food(self.value / float(num)) for _ in range(num)]
    
    @classmethod
    def sum_values(cls, instances):
        return sum(instance.value for instance in instances)

