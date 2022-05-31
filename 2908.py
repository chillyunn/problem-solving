import sys

A,B=map(str,sys.stdin.readline().split())

if int(A[::-1]) >int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])

#def reading(k):
#k=k[::-1]
#return int(k)
#print(max([reading(a),reading(b)]))