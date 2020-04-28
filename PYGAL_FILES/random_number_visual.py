import pygal
from random_number import Die

# creation the two dies with 6 walls
die_1 = Die()
die_2 = Die()

# make some number of rolls and pull them on the list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# results visualization
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Results of 2 dies rolls of 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequencies of result occurrence"

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_dies_visual.svg')