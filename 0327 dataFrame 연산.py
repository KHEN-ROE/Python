import pandas as pd

#dataFrame 연산
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
data2 = {'A': [9, 8, 7], 'B': [6, 5, 4], 'C': [3, 2, 1]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# 기본 연산
print(df1 + df2)
# 결과:
#    A  B  C
# 0 10 10 10
# 1 10 10 10
# 2 10 10 10

# 집계 함수
print(df1.mean()) # 결과: A    2.0, B    5.0, C    8.0, dtype: float64
print(df1.mean(axis=1)) # 결과: 0    4.0, 1    5.0, 2    6.0, dtype: float64
