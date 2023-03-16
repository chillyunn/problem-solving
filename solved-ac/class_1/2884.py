import sys

H,M = map(int,sys.stdin.readline().split())

if M<45:
    if H==0:
        H=23
        M=60-45+M
    else:
        H-=1
        M=60-45+M
else:
    M=M-45
print(H,M)

#------------------------
#x=a*60+b-45
#print(x//60%24,x%60)