from sys import stdin as f
import sys
sys.setrecursionlimit(10 ** 6)
f = open('testcase.txt', 'r')

n, m = list(map(int, f.readline().split()))

arr = [list(map(int, f.readline().split())) for i in range(m)]

parent = [i for i in range(n+1)]

def getparent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getparent(parent, parent[x])
        return parent[x]

def union_parent(parent, a, b):
    a = getparent(parent, a)
    b = getparent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def findparent(parent, a, b):
    a = getparent(parent, a)
    b = getparent(parent, b)
    if a == b:
        return "YES"
    else :
        return "NO"

for i in range(len(arr)):
    if arr[i][0] == 0:
        union_parent(parent, arr[i][1], arr[i][2])
    else:
        print(findparent(parent,arr[i][1], arr[i][2]))

