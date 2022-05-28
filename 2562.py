import sys

li=[]

for i in range(9):
    li.append(int(sys.stdin.readline()))

li_max=max(li)
print(li_max)
print(li.index(li_max)+1)