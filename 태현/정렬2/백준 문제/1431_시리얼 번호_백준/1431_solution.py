from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])

arr = [[0,0,f.readline().split()] for i in range(n)]

for i in range(len(arr)):
    arr[i][0] = len(arr[i][2][0])
    for j in range(len(arr[i][2][0])):
        # print(arr[i][2][0][j])
        if ord(arr[i][2][0][j]) >= 49 and ord(arr[i][2][0][j]) <= 57:
            arr[i][1] += int(arr[i][2][0][j])

print(arr)
arr.sort(key = lambda x : (x[0], x[1], x[2]))
for i in range(len(arr)):
    print(arr[i][2][0])
