import sys

def add(i):
    if i==0:
        return 0
    else:
        return i+add(i-1)

for i in range (int(sys.stdin.readline())):
    read = list(sys.stdin.readline().split('X'))
    result=0
    for i in range (len(read)):
        result+= add(read[i].count("O"))
    print(result)