from sys import stdin as f
from collections import deque
f = open('testcase.txt', 'r')
_ = f.readline()
arr1 = list(map(int,f.readline().split()))
arr2 = list(map(int,f.readline().split()))
ret = deque()
n = len(arr1)
m = len(arr2)
arr1_idx = 0
arr2_idx = 0
for i in range(n+m):
    if arr1_idx == n:
        while arr2_idx < m:
            ret.append(arr2[arr2_idx])
            arr2_idx += 1
        break
    elif arr2_idx == m:
        while arr1_idx < n:
            ret.append(arr1[arr1_idx])
            arr1_idx += 1
        break
    elif arr1[arr1_idx] < arr2[arr2_idx]:
        ret.append(arr1[arr1_idx])
        arr1_idx += 1

    elif arr1[arr1_idx] > arr2[arr2_idx]:
        ret.append(arr2[arr2_idx])
        arr2_idx += 1

    elif arr1[arr1_idx] == arr2[arr2_idx]:
        ret.append(arr1[arr1_idx])
        ret.append(arr2[arr2_idx])
        arr1_idx += 1
        arr2_idx += 1

while len(ret) != 0:
    print(ret.popleft(), end = ' ')
