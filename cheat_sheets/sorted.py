import Self_use

zork = [1,45,67,43,68,23]
#prints in ascending order
print(sorted(zork))
#prints in descending order
print(sorted(zork, reverse = True))

animals = [
{'type': 'penguin', 'name': 'Stephanie', 'age': 8},
{'type': 'elephant', 'name': 'Devon', 'age': 3},
{'type': 'puma', 'name': 'Moe', 'age': 5},
... ]

print(sorted(animals, key=lambda animal: animal['age']))