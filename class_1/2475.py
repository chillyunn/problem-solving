import sys

li = list(map(int,sys.stdin.readline().split()))

for i in range (len(li)):
    li[i] = li[i]*li[i]

print(sum(li)%10)
