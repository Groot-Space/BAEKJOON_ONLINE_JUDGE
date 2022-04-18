from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])

arr = deque(map(int,f.readline().split()))
d = [0] * (len(arr)+1)
arr.appendleft(0)

for i in range(1,n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[j] + 1, d[i])




print(max(d))