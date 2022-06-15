import sys

read= sys.stdin.readline().strip()
alphabet=[-1] * 26
for i in range (len(read)):
    if(alphabet[ord(read[i])-97] == -1):
        alphabet[ord(read[i])-97]=i
for i in range (len(alphabet)):
    print(alphabet[i],end=' ')


#-------------------------
# a = "abcdefghijklmnopqrstuvwxyz"
# for i in a:
#     print(read.find(i),end=' ')