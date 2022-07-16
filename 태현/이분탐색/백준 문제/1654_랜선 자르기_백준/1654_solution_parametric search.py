from sys import stdin as f
import sys
sys.setrecursionlimit(10 ** 6)
f = open('testcase.txt', 'r')
k, n = list(map(int,f.readline().split()))
arr = [int(f.readline().split()[0]) for i in range(k)]
arr.sort()

st = 1
en = (2 ** 31) - 1
mid = (st + en) // 2


