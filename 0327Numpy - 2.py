#파일 입출력
#NumPy 배열을 파일로 저장하고 읽어오기
import numpy as np

# 단일 배열 저장
arr1 = np.array([1, 2, 3, 4, 5])
np.save('arr1.npy', arr1)

# 다중 배열 저장
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([10, 20, 30, 40, 50])
np.savez('arr.npz', arr2=arr2, arr3=arr3)

# 배열 불러오기
loaded_arr1 = np.load('arr1.npy')
loaded_data = np.load('arr.npz')
loaded_arr2 = loaded_data['arr2']
loaded_arr3 = loaded_data['arr3']

# 정규 분포
arr1 = np.random.normal(0, 1, size=10)
print(arr1)
'''
[-1.03175853 -0.26330108  0.50114289  0.43128428  1.52632134
 -0.11669154 -0.38778772 -0.58322862  0.1852227  -1.12919514]
'''

# 균등 분포
arr2 = np.random.uniform(0, 1, size=10)
print(arr2)
'''
[0.3082703  0.59827088 0.61679035 0.3049514  0.10465949
 0.95647913 0.52484807 0.62345654 0.36863133 0.66491068]
'''

# 이항 분포
arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)
'''
[6 7 6 3 7 3 6 3 7 3] #0.5확률로 설정했을 때 성공률
'''

# 포아송 분포
arr4 = np.random.poisson(3, size=10)
print(arr4)
'''
[2 2 2 6 2 1 1 1 1 6]
'''
