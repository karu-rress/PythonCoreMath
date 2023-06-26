import matplotlib.pyplot as plt

x = [i for i in range(1, 8)]
y = [64.3, 63.8, 63.6, 64.0, 63.5, 63.2, 63.1]

plt.plot(x, y, marker='x')
plt.grid(color='0.8')
plt.show()


