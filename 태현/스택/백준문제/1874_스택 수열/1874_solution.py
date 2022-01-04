from collections import deque
from sys import stdin as f

f = open('testcase.txt','r')

n = int(list(f.readline().split())[0])
m = 100001
stack = deque()
target = int(list(f.readline().split())[0])
count = 0 #출력 갯수

ret = deque()
for i in range(1, m):
    if n == count :
        break

    stack.append(i)
    ret.append('+')
    while len(stack) != 0 and stack[-1] == target and n > count:
        stack.pop()
        ret.append('-')
        count += 1
        if n > count : target = int(list(f.readline().split())[0])


if count < n:
    print('NO')
else :
    for i in ret:
        print(i)