from sys import stdin as f

f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
arr = [ 0 for i in range(10001)]

for i in range(n):
    arr[int(f.readline().split()[0])] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
