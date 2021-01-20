from sys import stdin
import sys
sys.setrecursionlimit(15000)
def merge_sort(arr,st,ed,ret):
    if st+1 == ed:
        return arr
    m = (ed + st) // 2
    arr = merge_sort(arr, st, m, ret)
    arr = merge_sort(arr, m, ed, ret)
    _idx1 = st
    _idx2 = m
    for i in range(st,ed):
        if _idx1 == m:
            ret[i] = arr[_idx2]
            _idx2 += 1

        elif _idx2 == ed:
            ret[i] = arr[_idx1]
            _idx1 += 1
        elif arr[_idx1] <= arr[_idx2]:
            ret[i] = arr[_idx1]
            _idx1 += 1
        elif arr[_idx1] > arr[_idx2]:
            ret[i] = arr[_idx2]
            _idx2 += 1

    for i in range(st,ed):
        arr[i] = ret[i]

    return arr
test = int(stdin.readline())
arr = []
for i in range(test):
    arr.append(int(stdin.readline()))
ret = [0 for i in range(len(arr))]
arr = merge_sort(arr, 0, len(arr),ret)
for i in arr:
    print(i)
