from sys import stdin as f
from bisect import bisect_left
f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
arr = list(map(int,f.readline().split()))

_arr = sorted(list(set(arr)))

for i in range(len(arr)):
    ans = bisect_left(_arr,arr[i])
    print(ans , end = ' ')