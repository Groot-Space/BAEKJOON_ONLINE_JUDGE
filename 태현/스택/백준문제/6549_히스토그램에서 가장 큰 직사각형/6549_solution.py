from sys import stdin as f
from collections import deque
f = open('tsetcase.txt','r')
while 1:
    k = int(f.readline().split()[0])
    if k == 0:
        break

    mx = 0
    squares = list(map(int,f.readline().split()))
    stack = deque()
    continues = 1
    for i in range(len(squares)):
        if i == 0:
            stack.append(squares[i])
            mx = stack[-1]
        else :
            if stack[-1] > squares[i]:
                stack.append(squares[i])
                continues = 1
            elif stack[-1] <= squares[i]:
                stack