from food import Food
from resources import Resource
from creature import Creature
from dove import Dove, Hawk
import csv

def daily_cycle(creatures, resource):
    resource.assign_food(creatures)
    for pair in resource.pairs:
        pair.food_distribute()
    
    return Creature.get_all_creatures()

def data_collection(data, x, y, z):
    data["x"]["data"].append(x)
    data["y"]["data"].append(y)
    data["z"]["data"].append(z)


def main():
    all_creatures = [Dove('Dove')]
    data = {"x":{"name": "Day", "data": []}, "y":{"name": "Population", "data": []}, "z":{"name": "Dove", "data": []}}
    days_total = 10

    day = 0
    population = len(all_creatures)
    dove = len(Dove.get_all_creatures())
    data_collection(data, day, population, dove)

    for i in range (days_total):
        all_creatures = daily_cycle(all_creatures, Resource(60))
        day += 1
        population = len(all_creatures)
        dove = len(Dove.get_all_creatures())
        data_collection(data, day, population, dove)
    
    all_creatures += [Hawk('Hawk')]

    for i in range (days_total):
        all_creatures = daily_cycle(all_creatures, Resource(60))
        day += 1
        population = len(all_creatures)
        dove = len(Dove.get_all_creatures())
        data_collection(data, day, population, dove)


    
    with open('data.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
        writer = csv.writer(csvfile)
    
    # Write the header row
        writer.writerow([data["x"]["name"], data["y"]["name"], data["z"]["name"]])
    
    # Write each row of data
        for i in range(len(data["x"]["data"])):
            writer.writerow([data["x"]["data"][i], data["y"]["data"][i], data["z"]["data"][i]])


if __name__ == '__main__':
    main()