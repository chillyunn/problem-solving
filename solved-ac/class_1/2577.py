import sys
li=[]
for i in range (3):
    li.append(int(sys.stdin.readline()))
result= li[0]*li[1]*li[2]

li2=[]
while result>=1:
    li2.append(int(result%10))
    result/=10
for i in range(10):
    print(li2.count(i))
