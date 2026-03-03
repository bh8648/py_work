# random_module.py

import random
random.seed(42)

a = random.random()
print(a)

animals = ["dog", 'cat', 'hedgehog', 'tiger', 'lion']

print(random.choice(animals))


print("----------------------------")
print(random.sample(animals, 2))
print(random.sample(animals, 3))

print("----------------------------")
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))
print(random.randint(1, 45))



