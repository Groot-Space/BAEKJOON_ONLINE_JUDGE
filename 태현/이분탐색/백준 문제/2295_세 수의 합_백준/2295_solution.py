from sys import stdin as f
from collections import deque
f = open('testcase.txt','r')
n = int(f.readline().split()[0])
arr = deque()
for i in range(n):
    arr.append(int(f.readline().split()[0]))

