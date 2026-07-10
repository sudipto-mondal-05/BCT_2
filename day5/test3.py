import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 5, 10, 25]
plt.bar(x, y)
plt.savefig('plot.png')
print("Plot saved to plot.png")