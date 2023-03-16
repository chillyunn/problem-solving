import sys

read = list(sys.stdin.readline().strip('\n').upper())
read_set=set(read)
value_max=1
result=set()

for i in read_set:
    if read.count(i) >=value_max:
        if read.count(i) >value_max:
            value_max=read.count(i)
            result.clear()
            result.add(i)
        else:
            result.add(i)

if len(result) >= 2:
    print("?")
else:
    print(result.pop())