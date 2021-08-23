arr = [ i for i in range(10)]
target = 4
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    while 1:
        if start > end:
            return 1
        elif arr[mid] == target:
            return mid

        elif arr[mid] > target:
            start = mid + 1
            mid = (start + end) //2

        else:
            end = mid - 1
            mid = (start + end) // 2

print(binary_search(arr, target))

import bisect


print(bisect.bisect(arr, target) -1)