import sys

N= int(sys.stdin.readline())

for i in range (N):
    for j in range (i+1):
        print("*",end="")
    print()

#----------------------
# for i in range(1,N+1):
#     print("*"*i)