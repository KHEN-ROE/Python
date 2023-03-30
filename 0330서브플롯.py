#서브플롯
import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성. 틀을 잡고 그래프를 바로 넣을 수도 있다
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# 첫 번째 서브플롯
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()
