import csv,os

f = open('a.csv' ,'r' )

new = csv.reader(f)

f.seek(0)
a_list = []
for i in new:
    a_list.append(i)

print(a_list)