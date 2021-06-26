from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')
_ = f.readline()
arr = list(map(int,f.readline().split()))

mx = max(arr)
dct = dict()
for i in range(len(arr)):
    dct[arr[i]] = i+1

stack = deque()

for i in range(len(arr)):
    if i == 0:
        stack.append(arr[i])
        print(0, end = ' ')
    else :
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()
        stack.append(arr[i])
        idx = len(stack)-2

        if len(stack) == 1:
            print(0, end=' ')
            continue
        else :
            stack.append(arr[i])

        print(dct[stack[idx]], end =' ')

