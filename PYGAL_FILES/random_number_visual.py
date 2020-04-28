from random_number import Die

# creation the die with 6 walls
die = Die()

# make some number of rolls and pull them on the list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)