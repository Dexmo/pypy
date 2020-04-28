import pygal
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

# results visualization
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Results of 1 die rolls of 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequencies of result occurrence"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')