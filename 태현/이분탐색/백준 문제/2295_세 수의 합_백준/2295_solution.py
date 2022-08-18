from sys import stdin as f
from collections import deque
f = open('testcase.txt','r')
n = int(f.readline().split()[0])
arr = deque()



for i in range(n):
    arr.append(int(f.readline().split()[0]))

two_arr = set()

for i in range(len(arr)):
    for j in range(i, len(arr)):
        two_arr.add(arr[i] + arr[j])

arr = list(arr)
arr.sort()
flag = 0


for i in range(len(arr)-1, -1, -1):
    for j in range(i+1):
        if arr[i] - arr[j] in two_arr:
            print(arr[i])
            flag = 1
            break
    if flag==1:
        break
