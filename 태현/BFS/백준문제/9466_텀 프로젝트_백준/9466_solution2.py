from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')
t = list(map(int,f.readline().split()))[0]

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


while t > 0:
    n = list(map(int,(f.readline().split())))[0]
    board = deque(list(map(int, f.readline().split())))
    board.appendleft(0)
    parent = deque([i for i in range(n+1)])
    for i in range(1,n+1):
        union(parent, i, board[i])

    print(parent)

    t -= 1