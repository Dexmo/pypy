import matplotlib.pyplot as plt

from randomwalk import RandomWalkClass

while True:
    rw = RandomWalkClass()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=15)
    # Change the color of first (green) and last (red) points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Removing the axis from figure
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another random walk? (y/n): ")
    if keep_running == 'n':
        break
