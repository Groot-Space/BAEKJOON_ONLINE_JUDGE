from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

def two_point(arr, k, check):
    end = 0
    mx = 0
    for start in range(len(arr)):
        while end < len(arr) and check[arr[end]] < k:
            tmp = end - start + 1
            if mx < tmp:
                mx = tmp
            check[arr[end]] += 1
            end += 1

        check[arr[start]] -= 1
    return mx


n, k = list(map(int, f.readline().split()))
arr = list(map(int, f.readline().split()))
# dist = deque()
check = [0 for i in range(100001)]
print(two_point(arr, k,check))
