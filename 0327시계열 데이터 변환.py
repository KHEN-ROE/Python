#데이터 전처리
#시계열 데이터 변환 - pd.to)datetime()
#문자열이나 다른 형식의 날짜와 시간 데이터를 datetime 형식으로 변환할 때 사용

import pandas as pd

data = {'date': ['2021-08-15', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)
print(df.info())
df['date'] = pd.to_datetime(df['date'])
print(df)
# Output:
#         date  value
# 0 2021-08-15    100
# 1 2021-08-16    200
# 2 2021-08-17    150

"""
문자열이 다른 형식으로 되어 있을 경우 이를 자동으로 감지 못 함. 
이때는 format 인자를 사용하여 문자열의 형식을 지정.
"""
"""
# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print(df)
"""
#pd.resample()  - 기존의 데이터셋을 새로운 시간 간격에 맞추어 변환
data = {'date': ['2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02', '2022-01-01', '2022-01-02', '2022-02-01', '2022-02-02', '2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'location': ['서울', '서울', '서울', '서울', '서울', '서울', '서울', '서울', '부산', '부산', '부산', '부산', '부산', '부산', '부산', '부산'],
        'PM10': [50, 40, 45, 55, 60, 65, 70, 80, 55, 45, 50, 60, 70, 75, 80, 90],
        'PM2.5': [25, 20, 22, 28, 30, 35, 40, 45, 30, 25, 28, 35, 40, 42, 45, 50]}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('M', on='date').mean(numeric_only=True)
df_monthly.dropna(inplace=True) #결측치 제거 해봄 
print(df_monthly)

