import re

# match 매서드

pattern = r'life'
script = 'life is so cool'

#print(re.match(pattern,script).group())

# split 매서드

data = 'a:3;b:2;c:6'

#print(re.split(r';',data))

# ly 로 끝나는 단어 추출하기

sentence = 'I have a lovely dog, really. I am not telling a lie'
pattern2 = r'\w+ly'

print(re.findall(pattern2,sentence))
