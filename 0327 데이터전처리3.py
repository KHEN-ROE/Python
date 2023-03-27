#데이터 형 변환 - astype()함수
import pandas as pd
"""
# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형

# 데이터프레임 정보 출력
print(df.dtypes)
"""

"""
#범주형 데이터
# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}

df = pd.DataFrame(data)

# gender 열을 category 형으로 변환
df['gender'] = df['gender'].astype('category')

# city 열을 category 형으로 변환
df['city'] = df['city'].astype('category')

# 카테고리별 데이터 개수 확인
print(df['gender'].value_counts())
print(df['city'].value_counts())

# 카테고리별 통계량 확인
print(df.groupby('gender').mean(numeric_only=True))
print(df.groupby('city').mean(numeric_only=True))
"""

"""
#.str 엑세서를 이용한 문자열 처리 예시
# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}
df = pd.DataFrame(data)

# 문자열 처리 작업
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할 
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True) #모든 글자 모든 공백을 뺀 나머. 즉 기호를 찾는 식#주의 : ^은 처음, [^]는 부정.  # 구두점, 기호 제거
df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df.iloc[:, 1:])
"""
"""
#열 및 행 조작
# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
df = df.loc[[4, 3, 2, 1, 0]]

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=True)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)
"""

"""
#데이터 병합 - concat
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True) #ignore_index 없으면 index정렬 안 됨

print(result)
"""
"""
#merge
#기본 조인 방법은 inner join(교집합)
left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

result = pd.merge(left, right, on='key', how='outer')

print(result)
"""

"""
#join
# 예시 데이터
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                     index=['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index=['K0', 'K1', 'K2', 'K3'])

# 인덱스를 기준으로 병합
result = left.join(right)

print(result)

#merge는 k를 기준으로, join은 index를 기준으로 병합 
"""


