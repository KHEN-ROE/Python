#데이터 그룹화
import pandas as pd
"""
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100]}

df = pd.DataFrame(data)

# count
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print(df.groupby('gender')[['score1', 'score2']].describe())
"""

"""
#agg
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': [1, 2, 3, 4, 5, 6, 7, 8],
    'D': [10, 20, 30, 40, 50, 60, 70, 80]
})

result = df.groupby(['A', 'B']).agg({'C': 'count', 'D': ['sum', 'mean']})
print(result)

#사용자 정의 함수 적용 가능
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
})

def my_func(x):
    return '-'.join(sorted(x))

result = df.groupby('A').agg({'B': my_func})

print(result)
"""

#Pivot_table
#데이터프레임에서 특정 열을 그룹화하여 행과 열을 피벗테이블 형태로 표현.
#위 데이터프레임에서 Name 열과 Date 열을 기준으로 Value 열의 평균을 계산
"""
df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob'],
    'Date': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Value': [10, 20, 15, 25, 30, 40, 35, 45]
})

result = df.pivot_table(values='Value', index='Name', columns='Date', aggfunc='mean')

print(result)
"""

#고객 데이터를 이용한 지역별, 연령대별 평균 소비 금액 집계
# 고객 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'], 
        'Age': [20, 30, 40, 50, 30, 40, 50, 60],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
df = pd.DataFrame(data)

# 피벗테이블 생성
result = pd.pivot_table(df, index='Region', columns=pd.cut(df['Age'], [10, 30, 50, 70]), values='Sales', aggfunc='mean')
                                                    #cut함수 사용 
print(result)

#cut 함수
#주어진 데이터를 일정한 구간으로 나누어 범주형 데이터로 변환하는 함수
import pandas as pd

# 나이 데이터 생성
ages = pd.DataFrame({'age': [22, 44, 65, 86, 27, 19, 51, 92, 33, 35, 38, 42, 14, 50, 78]})

# 연령대 구간 지정
bins = [0, 20, 40, 60, 80, 100]

# 연령대 카테고리 생성
age_categories = pd.cut(ages['age'], bins)

# 데이터프레임에 새로운 카테고리 열 추가
ages['age_categories'] = age_categories

# 결과 확인
print(ages)

result = pd.pivot_table(ages, index='age_categories', aggfunc='count')

print(result)
