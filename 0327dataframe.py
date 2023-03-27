#DataFrame
#2차원 테이블 형태의 자료구조
#인덱스와 열(column)로 구성된 데이터
import pandas as pd
import numpy as np

"""
# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print(df1)

# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df2)

# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)

# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print(df4)
"""
"""
# 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_csv('data.csv')
print(df5)
"""
"""
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 데이터프레임 정보 출력
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력
"""
"""
#DataFrame 인덱싱 및 슬라이싱
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)
print(df)
# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택
name_col = df.loc[:, 'name']
print(name_col)

# 열 선택 방법 5: iloc[]를 이용한 열 선택
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)
"""
#행선택
"""
query() 메소드 - 데이터프레임에서
특정 조건에 맞는 데이터를 선택하는 메소드
조건을 문자열로 입력
"""
"""
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)

sub_df = df.loc[df['age'] >= 30]
print(sub_df)

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)

# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)
"""

#부분 데이터 선택. at메소드 사용
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택
sub_df_1 = df.loc[df['age'] > 30, ['name', 'city']]
print(sub_df_1)

# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
sub_df_2 = df.query('age > 30')[['name', 'city']]
print(sub_df_2)

# 부분 데이터 선택 방법 3: 슬라이싱을 이용한 범위 지정
sub_df_3 = df.iloc[1:3, 1:3]
print(sub_df_3)

# 부분 데이터 선택 방법 4: iloc[]를 이용한 인덱스 지정
sub_df_4 = df.iloc[[1, 3], [0, 2]]
print(sub_df_4)

# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print(sub_df_5)

# 부분 데이터 선택 방법 6: at[]을 이용한 특정 위치 선택
val = df.at[1, 'age']
print(val)

