import matplotlib.pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]

plt.scatter(x_values, squares, s=40)
plt.plot(x_values, squares, 30)

plt.xlabel("Values", fontsize=12)
plt.ylabel("Square values", fontsize=12)
plt.title("SQUARES", fontsize=20)

plt.show()
