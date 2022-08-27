from sys import stdin as f
import bisect

f = open('testcase.txt', 'r')

n, m = f.readline().split()

arr1 = list(map(int,f.readline().split()))
arr2 = list(map(int,f.readline().split()))
arr1.sort()
arr2.sort()
ans = []
for num in arr1:
    right = bisect.bisect_right(arr2,num)
    left = bisect.bisect_left(arr2, num)
    if left - right == 0:
        ans.append(num)

if len(ans) != 0:
    print(len(ans))
    for num in ans:
        print(num, end = ' ')
else :
    print(0)