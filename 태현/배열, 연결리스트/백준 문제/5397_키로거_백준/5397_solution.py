f = open('키로거_테스트케이스.txt','r')
testcase = f.readline()
from sys import stdin
def solve(text):
    right = []
    left = []
    for i in text:
        if i == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif i == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif i == '-' and len(left) > 0:
            left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))

for i in range(int(testcase)):
    solve(f.readline().strip())
