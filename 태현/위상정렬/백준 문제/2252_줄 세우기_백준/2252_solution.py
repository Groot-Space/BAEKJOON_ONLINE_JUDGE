from sys import stdin as f
from collections import deque
f = open('testcase_줄 세우기.txt', 'r')

n, m = list(map(int, f.readline().split()))

students = [0 for i in range(n+1)]
graphs = [deque() for i in range(n+1)]
ret = deque()
for i in range(m):
    tmp = list(map(int, f.readline().split()))
    students[tmp[1]] += 1
    graphs[tmp[0]].append(tmp[1])

for i in range(len(students)):
    if students[i] == 0:
        ret.append(i)

i = 1
while i < len(ret):
    cur = ret[i]
    print(cur, end =' ')
    for j in range(len(graphs[cur])):
        students[graphs[cur][j]] -= 1
        if students[graphs[cur][j]] == 0:
            ret.append(graphs[cur][j])
    i += 1