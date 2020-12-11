import os, re, usecsv

# csv 파일 읽기(read)
total = usecsv.opencsv('popSeoul.csv')
newPop = usecsv.switch(total)

# 등록 외국인 비율 계산하기
i = newPop[1]

foreign = round(i[2]/(i[1] + i[2]) * 100, 1)
#print(foreign)

# 각 구의 외국인 비율 출력하기
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1] + i[2]) * 100, 1)
        # print(i[0],foreign)
    except:
        pass


# 외국인 비율이 3% 초과할 때만 출력해보기
i = newPop[1]
new = [['구','한국인','외국인','외국인비율']]
new.append([i[0],i[1],i[2],foreign])
# print(new)

for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1] + i[2]) * 100, 1)
        if foreign > 3:
            print(i[0],foreign)
    except:
        pass

# usecsv.writecsv('newPop.csv', new)