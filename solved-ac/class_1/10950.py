import sys

T=int(sys.stdin.readline())
li = list()
for i in range (T):
    A,B= map(int,sys.stdin.readline().split())
    li.append(A+B)

for i in li:
    print(i)



#--------------------------------------
#list(sum(map(int,n.split())) for n in sys.stdin)