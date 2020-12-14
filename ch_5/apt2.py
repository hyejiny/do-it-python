import pandas as pd
import re, os

# 판다스로 csv파일 불러오기
df = pd.read_csv('apt.csv', encoding= 'cp949')
# 일부분만 확인하기 
# print(df.head())
# print(df.tail())

# 조건 설정
# print(df.지역)
# print(df[df.면적 > 130])

# print(df.loc[:10,['아파트','가격']])
# print(df.loc[:,['아파트','가격']][df.가격> 40000])

#새로운 값 추가하기
df['단가'] = df.가격 / df.면적
# print(df.loc[:10,('가격','면적','단가')])

#데이터 정렬하기
# print(df.sort_values(by='가격').loc[:,('가격','지역')])
# print(df.sort_values(by='가격', ascending= False).loc[:,('가격','지역')])

#문자열 다루기(인덱스 출력)
print(df.지역.str.find('강릉'))