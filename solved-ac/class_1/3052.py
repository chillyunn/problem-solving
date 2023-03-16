import sys
li=set()
for i in range (10):
    li.add(int(sys.stdin.readline())%42)
print(len(li))

#li=[int(sys.stdin.readline())%42 for i in range (10)]
#print(len(set(li)))