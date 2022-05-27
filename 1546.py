from audioop import avg
from ctypes import sizeof
import sys

a = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
M=max(li)

for i in range(len(li)):
    li[i] = li[i]/M*100

print(sum(li)/a)

#----------------
#print(sum(li)/M*100/a)