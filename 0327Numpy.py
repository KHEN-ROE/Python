import numpy as np
# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5] # 주의 - 리스트가 아닌 배열이다.

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]

# 3차원 배열 생성
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)

# 4차원 배열 생성
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
print(arr4d)

#브로드캐스팅

#유니버셜 함수
arr = np.array([0, 1, 2, 3, 4])

# 제곱근 함수
print(np.sqrt(arr))  # [0.         1.         1.41421356 1.73205081 2.        ]

# 지수 함수
print(np.exp(arr))  # [ 1.          2.71828183  7.3890561  20.08553692 54.59815003]

# 로그 함수
print(np.log(arr+1))  # [0.         0.69314718 1.09861229 1.38629436 1.60943791]

#배열 변형 및 조작
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print(arr2d_transpose)

