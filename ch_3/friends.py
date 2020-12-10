import os,re,codecs

f = codecs.open('friends101.txt','r','utf-8')

script101 = f.read()

# print(script101[:100])

# 특정 등장인물의 대사 모으기

line = re.findall(r'Monica:.+',script101)
print(line[:3])

with open('Monica.txt','w',encoding='utf-8') as b:
    monica = ''
    for i in range(len(line)):
        monica += line[i] + '\n'
    b.write(monica)


# 등장인물 리스트 만들기

char = re.compile(r'[A-Z][a-z]+:')
a= set(re.findall(char,script101))

char_list = []
for i in a:
    char_list.append(i[:-1])

print(char_list)

# 지문만 출력하기

action = re.compile(r'\([A-Za-z].+[a-z|\.]\)')

c = re.findall(action,script101)
#
for i in c:
    print(i)

# 특정 단어의 예문만 모아 파일로 저장하기

sentences = f.readlines()

# lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('would',i)]
lines = []
for i in sentences:
    if re.match(r'[A-Z][a-z]+:',i):
        lines.append(i)

re2 = []
for i in lines:
    if re.search('would',i):
        re2.append(i)

print(re2)