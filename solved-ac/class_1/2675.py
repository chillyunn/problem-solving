# import sys

# T=int(sys.stdin.readline())
# for i in range(T):
#     input=sys.stdin.readline().split()
#     R=int(input[0])
#     S=str(input[1])
#     for j in range (len(S)):
#         print(S[j]*R,end="")
#     print()

#-----------------------
import sys

T=int(sys.stdin.readline())
for i in range(T):
    R,S=sys.stdin.readline().split()
    for j in S:
        print(j*int(R),end="")
    print()