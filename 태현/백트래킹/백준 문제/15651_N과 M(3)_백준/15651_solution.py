from sys import stdin as f
from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
n, m = list(map(int, f.readline().split()))

visited = [0 for i in range(n+1)]


def f_backtrack(n, m, tmp, visited):
    if len(tmp) == m:
        for i in tmp:
            print(i, end=' ')
        print()
    else :
        for i in range(1, n+1):
            tmp.append(i)
            f_backtrack(n, m, tmp, visited)
            tmp.pop()

tmp = deque()
ret = f_backtrack(n, m, tmp, visited)
