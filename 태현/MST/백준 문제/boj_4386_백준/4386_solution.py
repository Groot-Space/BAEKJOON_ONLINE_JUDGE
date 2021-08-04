from sys import stdin as f
from itertools import combinations

f = open('testcase.txt', 'r')

def get_cost(y1, x1, y2, x2):
    _1 = (y1 - y2) ** 2
    _2 = (x1 - x2) ** 2
    return (_1 + _2) ** 0.5

def get_parent(parent, a):
    if parent[a] == a:
        return a
    else :
        parent[a] = get_parent(parent,parent[a])
        return parent[a]

def union(parent,a , b):
    a = get_parent(parent,a)
    b = get_parent(parent,b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

def is_union(parent,a,b):
    a = get_parent(parent,a)
    b = get_parent(parent,b)
    if a == b:
        return True
    else:
        return False

n = int(f.readline().split()[0])

stars = [list(map(float, f.readline().split())) for i in range(n)]

_tmp = [i for i in range(n)]
stars_connections = list(combinations(_tmp, 2))

cost_board = []

mx = 0
for start, end in stars_connections:
    cost_board.append([start,end,get_cost(stars[start][0],stars[start][1],stars[end][0],stars[end][1])])
    mx = max([start,end,mx])

cost_board.sort(key = lambda x : x[2])

parent = [i for i in range(mx+1)]

total_cost = 0
for a, b, c in cost_board:
    if is_union(parent,a,b) == False:
        union(parent,a,b)
        total_cost += c

print(round(total_cost,2))