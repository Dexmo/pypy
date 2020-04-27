import matplotlib.pyplot as plt

from randomwalk import RandomWalkClass

while True:
    rw = RandomWalkClass()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)
    plt.show()

    keep_running = input("Create another random walk? (y/n): ")
    if keep_running == 'n':
        break
