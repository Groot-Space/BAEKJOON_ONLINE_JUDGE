from sys import stdin as f
import sys
sys.setrecursionlimit(10**6)

f = open('testcase.txt', 'r')
n, m = list(map(int,f.readline().split()))
arr = list(map(int,f.readline().split()))

d = [0 for i in range(n+1)]


for i in range(1,len(d)):
    d[i] = d[i-1]  + arr[i-1]

for i in range(m):
    tmp = list(map(int,f.readline().split()))
    print(d[tmp[1]] - d[tmp[0]-1])
