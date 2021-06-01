from sys import stdin as f
import sys
sys.setrecursionlimit(10**6)

f = open('testcase.txt', 'r')
n, m = list(map(int,f.readline().split()))
arr = list(map(int,f.readline().split()))

q = []
for i in range(m):
    tmp = list(map(int,f.readline().split()))
    q.append(tmp)

d = [[0 for j in range(n)] for i in range(n)]

def dynamic(n, d, arr):
    if n == 0:
        for i in range(len(d[n])):
            d[n][i] = arr[0]
        return d
    else :
        dynamic(n-1,d,arr)
        for i in range(len(d[n])):
            if i == 0:
                d[n][i] = arr[n]
            else:
                d[n][i] = d[n-1][i-1] + arr[n]
        return d

d = dynamic(n-1,d,arr)
for i in range(len(q)):
    print(d[q[i][1]-1][q[i][1]-q[i][0]])