from sys import stdin as f
from collections import deque
from bisect import bisect_left, bisect_right
f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
arr = list(map(int,f.readline().split()))
query = int(f.readline().split()[0])
chain = deque()
def search_duplicate(arr, target):
    left = bisect_left(arr, target)
    right = bisect_right(arr, target)
    if (right - left) == 1:
        return True
    else :
        return False

start, end = list(map(int,f.readline().split()))

for i in range(query):
    start, end = list(map(int,f.readline().split()))
    chain = deque()
    for j in range(start, end):

