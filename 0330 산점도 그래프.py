#산점도 그래프
import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)

# 그래프 타이틀과 축 라벨 설정
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
