# 백준 1406번 -2 2개의 스텍을 이용한 문제풀이

import sys

stack1 = list(sys.stdin.readline())
stack1 = stack1[:-1]
stack2 = []

count = int(sys.stdin.readline())
print(stack1,count)
while count > 0:
    oper = list(sys.stdin.readline().split())
    print(oper)

    if oper[0] == 'L':
        if len(stack1) > 0:
            stack2.append(stack1[-1])
            stack1 = stack1[:-1]
    elif oper[0] == 'D':
        if len(stack2) > 0:
            stack1.append(stack2[0])
            stack2 = stack2[1:]
    elif oper[0] == 'B':
        if len(stack1) > 0:
            stack1 = stack1[:-1]
    else:
        stack1.append(oper[1])
    count -= 1
s1 = ''
s2 = ''
if len(stack1) != 0:
    s1 = ''.join(stack1)
if len(stack2) != 0:
    s2 = ''.join(stack2)

print(s1 + s2)
