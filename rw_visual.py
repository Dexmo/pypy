import matplotlib.pyplot as plt

from randomwalk import RandomWalkClass

while True:
    rw = RandomWalkClass()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break
