import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1.0, 1.01, 0.01) # 범위: [-1.00, 1.01)
y = 3*x # 자동으로 x의 각 요소에 3을 곱해 y 생성

plt.plot(x, y)
plt.grid(color='0.8')
plt.show()