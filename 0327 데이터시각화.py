import pandas as pd

#한글있으면 인코딩 해줘야 함 
df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="cp949") #혹은 "euc-kr"

#print(df.head(20)) #앞에서 20개
#print(df.columns)
"""
name_age_col = df.iloc[:, [0, 1, 6, 7]]
print(name_age_col)
"""
"""
sub_df = df.loc[df['미세먼지농도(㎍/㎥)'] >= 30]
print(sub_df)
"""

"""
sub_df1 = df.loc[(df['미세먼지농도(㎍/㎥)'] > 5) & (df['초미세먼지농도(㎍/㎥)'] > 30)]
print(sub_df1)
"""

sub_df_2 = df.loc[(df['미세먼지농도(㎍/㎥)'] > 5)].loc[:,['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']] #.loc해서 조건 계속 추가 가능
print(sub_df_2)
