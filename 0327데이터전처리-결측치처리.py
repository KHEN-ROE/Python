#데이터 전처리
#결측치 처리 - 대체, 제거
import pandas as pd
import numpy as np

# 예제 데이터
data = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull())
# 결과:
#        A      B      C
# 0  False  False  False
# 1   True  False  False
# 2  False   True  False

# 결측치 대체
filled_df = df.fillna(0)
print(filled_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7
# 1  0.0  5.0  8
# 2  3.0  0.0  9

# 결측치 제거
dropped_df = df.dropna()
print(dropped_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7
