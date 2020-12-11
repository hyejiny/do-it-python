## ch4. CSV파일로 데이터 다루기

📘 CSV 데이터 읽기, 쓰기 및 가공하기 

> 파이썬 사용의 목적은 데이터를 잘 다루기 위함이다. 특히 대량의 데이터를 다양한 조건식으로 가공하거나, 통계적으로 분석할 때 사용된다.



#### 1. CSV 데이터란?

* CSV : 쉼표로 나눠진 값을 저장한 데이터
* 원형 그대로 가공하기 좋은 데이터 형식



#### 2. 파이썬으로 CSV 파일 읽고 쓰기

* csv 모듈로 파일을 가져와 파이썬에서 가공하기 좋은 형태인 리스트형으로 만든다.

```python
import csv, os, re

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

def writecsv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)
```



#### 3. CSV 파일 안의 문자를 숫자로 전환하기

* 정규 표현식 활용



#### 📌실습

* 서울 내 외국인 인구 비율 조사

  * `foreing.py`

  * 서울시 구별 주민등록인구 통계 활용

* 부동산 실거래가 검색

  * `apt.py`
  * 국토 교통부 실거래가 공개시스템 '부동산 실거래'정보 활용

* 번역한 예문 표로 저장하기

  * `trans.py`
  * googletrans 라이브러리



💡 

이 책의 저자는 csv파일을 가공하는 과정을 계산기를 두드리는 일이라고 표현한다. 뒷 부분에서 배우는 넘파이, 판다스로 더 쉽게 구현이 가능하다는 이유떄문이다.

그러나, 이 과정을 통해 반복문, 조건문 등을 활용하여 데이터에서 원하는 정보를 가져오는 연습을 할 수 있어서 좋았다.