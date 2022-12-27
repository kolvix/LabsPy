import json
from random import randint, choice
from pprint import pprint


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class Juice:
    def __init__(self):
        self.brand = choice(
            ['Moya semya', 'Lubimiy', 'Dobriy','Santal' , 'Auchan', 'Sadi pridoniya', 'J7', 'Globus', 'Natur Pur'])
        self.taste = choice(
            ['Apple', 'Multifrukt', 'Tomate', 'Vinograd', 'Orange'])
        self.grade = randint(1, 5)


data = {
    'Juice': []
}

for i in range(30):
    data['Juice'].append(Juice().__dict__)

n_data = read('lab2_data.json')
print(n_data['Juice'][29])
g = Juice()

g.name = n_data['Juice'][4]['taste']

print(g.name)

input()