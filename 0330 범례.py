#범례추가 - legend 함수
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed', label='Sine')
plt.plot(x, y2, linestyle='dashdot', label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')
plt.show()
