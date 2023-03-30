#선그래프
import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=5)

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()
