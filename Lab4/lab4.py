from functools import reduce
import csv

with open("foreign_names.csv", "r") as file:
    keys = file.readline()
    reader = csv.reader(file, delimiter=";")
    dataset = [x for x in reader]
keys = list(keys.split(","))
women = list(map(lambda x: x[3] == 'Female', dataset))
print(women.count(True))