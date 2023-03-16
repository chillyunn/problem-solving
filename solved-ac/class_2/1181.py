import sys

N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    input = sys.stdin.readline().strip()
    if input not in arr:
        arr.append(input)

def quickSort(arr):
    if len(arr) <= 1: return arr

    pivot, tail = arr[0],arr[1:]

    leftSide = [x for x in tail if len(x) <= len(pivot)]
    rightSide = [x for x in tail if len(x) > len(pivot)]

    return quickSort(leftSide) + [pivot] + quickSort(rightSide)

# quickSort(arr)
print(arr)