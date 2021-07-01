from sys import stdin as f
import sys
sys.setrecursionlimit(10**6)

f = open('testcase.txt', 'r')

# n = 정점 갯수
# m = 간선 갯수
n, m = list(map(int,f.readline().split()))

arr = [list(map(int, f.readline().split())) for i in range(m)]

high = max(arr, key = lambda x: x[0])[0]
high2 = max(arr, key = lambda x: x[1])[1]

if high < high2:
    high = high2

parent = [i for i in range(high + 1)]

def get_parent(parent, x):
    if parent[x] == x:
        return x
    else :
        parent[x] = get_parent(parent, parent[x])
        return parent[x]

def union(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def check_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return 1
    else :
        return 0

arr = sorted(arr, key = lambda x : x[2])

count = 0
total = 0
while count < len(arr):
    if check_parent(parent,arr[count][0],arr[count][1]) == 0:
        union(parent, arr[count][0], arr[count][1])
        total += arr[count][2]
    count += 1

print(total)