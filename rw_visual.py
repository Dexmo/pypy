import matplotlib.pyplot as plt

from randomwalk import RandomWalkClass

rw = RandomWalkClass()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
