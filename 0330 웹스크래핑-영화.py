#웹스크래핑 - 다음 영화 예매 순위 정보를 출력하는 예시

import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

ol = soup.select_one('.list_movieranking')
li_list = ol.find_all('li') #ol태그안에 있는 li태그를 리스트 형태로 모두 가져온다.
print(li_list)

movie = []

for li in li_list: #리스트 안에 있는 태그를 뽑아낸다.
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1] #슬라이싱 이용하여 %자름.
    mvdate = li.select_one('.txt_info > .txt_num').text
    
    movie.append([rank, name, see, grade, num, mvdate])
    
print(movie)

import pandas as pd

df = pd.DataFrame(movie, columns = ['순위', '영화명', '관람가','평점','예매율','개봉일'] )

df.to_csv('movie_info.csv', index=False, encoding='cp949') #데이터프레임 객체를 csv 파일로 변환.

df = pd.read_csv('movie_info.csv', encoding='cp949') # read_csv로 읽어오면 숫자로 된 문자는 알아서 숫자로 변환해줌

print(df.info())

print(df[df['평점'] > 8]) #데이터 타입이 object(문자열)이라 에러남. 그래서 전처리 해야함. 혹은 read_csv로 읽어오던지

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

#날짜형 데이터로 형변환
df['개봉일'] = pd.to_datetime(df['개봉일'], format = '%y.%m.%d')
#print(df.info())

df_weekly = df.resample('W', on = '개봉일').mean() # 숫자가 아니면 warning 떠서 numeric_only 넣어줌
#결측치 제거(0으로 채워줌)
df_weekly = df_weekly.fillna(0)
print(df_weekly)
plt.plot(df_weekly.index, df_weekly['예매율'], label='예매율')
plt.xlabel('날짜')
plt.ylabel('예매율')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')
plt.show()

#평가 - 웹크롤링해서 판다스로 저장하고 분석해서 그래프로 표현

