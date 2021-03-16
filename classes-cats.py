# Assignment

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.".  x will be the oldest cat age by using the function in #2


# ********************************************* My solution *******************************

# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Sneaky', 3)
cat2 = Cat('Houdini', 4)
cat3 = Cat('Ginger', 2)

# 2 Create a function that finds the oldest cat

def oldest_cat():
  list = [cat1.age, cat2.age, cat3.age]
  oldest = max(list)
  return oldest

# 3 Print out: "The oldest cat is x years old.".

print(f'The oldest cat is {oldest_cat()}-years old.')

# ********************************************* Andrei's solution *******************************

# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)

# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)

# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")