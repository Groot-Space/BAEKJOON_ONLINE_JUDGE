from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

k = int(f.readline().split()[0])
line = []
total_count = 0
for i in range(k):
    line.append(int(f.readline().split()[0]))

for j in range(len(line)-1):
    stack = deque()
    stack.append(line[j])
    stack.append(line[j+1])
    total_count += 1
    for i in range(j+2,len(line)):
        if line[j] < stack[-1] :
            break
        elif stack[-1] < line[i]:
            stack.append(line[i])
            total_count += 1

print(total_count)