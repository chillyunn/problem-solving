import sys

li = list()
while 1:
    try:
        li.append(sum(map(int,sys.stdin.readline().split())))
    except:
        break
for i in li:
     print(i)