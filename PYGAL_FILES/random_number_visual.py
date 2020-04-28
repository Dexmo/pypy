from random_number import Die

# creation the die with 6 walls
die = Die()

# make some number of rolls and pull them on the list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# results analysis
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)