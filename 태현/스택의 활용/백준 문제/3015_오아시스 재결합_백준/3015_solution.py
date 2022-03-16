from sys import stdin as f
from collections import deque

f = open('testcase2.txt', 'r')

k = int(f.readline().split()[0])
line = []
total_count = 0
for i in range(k):
    line.append(int(f.readline().split()[0]))

# print(line)
stack = deque()


for i in range(0,len(line)):
    if len(stack) == 0:
        stack.append([line[i], 1])
        continue

    elif stack[-1][0] == line[i]:
        stack[-1][1] += 1
        continue

    while len(stack) != 0 and stack[-1][0] < line[i]:
        if stack[-1][1] == 1:
            stack.pop()
            total_count += 1

        else:
            total_count += stack.pop()[1] - 1
            total_count += 1

    if len(stack) != 0:
        stack.append([line[i], 1])
        total_count += 1

    else :
        stack.append([line[i],1])

print(total_count)

