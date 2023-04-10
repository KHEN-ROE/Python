#네이버 증권에서 코스피 시가총액 상위 50개 종목 추출

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#table 태그 아래, tbody 태그 아래, tr 태그 가져옴
data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
data = []
for row in data_rows:
    columns = row.find_all("td") # tr 태그 안에 td태그 가져옴
    if len(columns) <= 1: #필요없는 공백은 skip
        continue
    data.append([column.get_text().strip() for column in columns]) #리스트에 데이터 저장


import pandas as pd

#데이터 프레임 생성
df = pd.DataFrame(data, columns = ['N', '종목명', '현재가', '전일비', '등락률', '액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE', '토론실'])

#csv파일로 저장
#df.to_csv('시총상위50.csv', index=False, encoding='cp949')

df = pd.read_csv('시총상위50.csv', encoding='cp949')

print(df.info())

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

#시가총액순으로 정렬
df_sorted = df.sort_values(by=['시가총액'], ascending=True)
#print(df_sorted)
top_10 = df_sorted[:10]

# 막대그래프 생성
plt.bar(top_10['종목명'], top_10['시가총액'])

plt.title('코스피 시가총액 상위 10개 종목')
plt.xlabel('종목명')
plt.ylabel('시가총액')

plt.show()