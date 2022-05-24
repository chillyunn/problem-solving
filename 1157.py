from asyncio.windows_events import NULL
from statistics import pvariance
import sys

read = sys.stdin.readline().strip('\n').upper()
readDict={}
li=[]
for i in set(read):
    readDict[i]=read.count(i)
reverseDict={v:k for k,v in readDict.items()}
dict_max=readDict.get(max(readDict))
for i in readDict:
    
    li.append(readDict.get(i))

if li.count(dict_max) >=2:
    print("?")
else:
    print(reverseDict.get(dict_max))