import matplotlib.pyplot as plt
import numpy as np

th = np.arange(0, 360)

# 매개변수 방정식. x = r cos th, y = r sin th
x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x, y)
plt.axis('equal')
plt.grid(color='0.8')
plt.show()
