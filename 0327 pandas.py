#pandas
import pandas as pd

#series
# Series 생성
# 리스트 사용
data = pd.Series([1, 2, 3, 4])
print(data)

# 문자열 인덱스 사용
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

# 딕셔너리 사용
data1 = {'a': 1, 'b': 2, 'c': 3 ,'d': 4}
s1 = pd.Series(data1)
print(s1)

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50

# 시리즈 생성
data1 = {'a': 1, 'b': 2, 'c': 3}
data2 = {'a': 10, 'c': 30, 'd': 40}
s1 = pd.Series(data1)
s2 = pd.Series(data2)

# 덧셈 연산
s = s1 + s2
print(s)  # a    11.0, b     NaN, c    33.0, d     NaN
           # dtype: float64

# 뺄셈 연산
s = s1 - s2
print(s)  # a    -9.0, b     NaN, c   -27.0, d     NaN
           # dtype: float64

# 곱셈 연산
s = s1 * s2
print(s)  # a    10.0, b     NaN, c    90.0, d     NaN
           # dtype: float64

# 나눗셈 연산
s = s1 / s2
print(s)  # a    0.1 , b     NaN, c    0.1 , d     NaN
           # dtype: float64

# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 집계 함수 예시
print(s.sum())  # 150
print(s.mean())  # 30.0
print(s.std())  # 15.811388300841896
print(s.max())  # 50
print(s.min())  # 10

