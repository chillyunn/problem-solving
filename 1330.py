import sys

a,b= sys.stdin.readline().split()

if int(a)>=int(b):
    if int(a)>int(b):
        print(">")
    else:
        print("==")
else:
    print("<")

#=================================

#a,b= map(int,sys.stdin.readlin().split())