from sys import stdin as f
import sys
sys.setrecursionlimit(10 ** 6)
f = open('testcase.txt', 'r')

k, n = list(map(int,f.readline().split()))

arr = [int(f.readline().split()[0]) for i in range(k)]

arr.sort()

def check(arr, mid, n):
    cur = 0
    for i in range(len(arr)):
        cur += arr[i] // mid
    if cur < n:
        return 1
    else :
        return 0

st = 1
en = (2 ** 31) -1
mid = (st + en) // 2
while st < en:
    if check(arr,mid,n) == 1:
        en = mid - 1
        mid = (st + en) // 2
    else :
        st = mid
        mid = (st + en + 1) // 2

print(mid)