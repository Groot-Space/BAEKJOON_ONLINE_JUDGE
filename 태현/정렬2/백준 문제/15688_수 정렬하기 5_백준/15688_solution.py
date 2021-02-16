f = open('testcase.txt', 'r')
k = int(f.readline())
m = 1000000
arr = [0 for i in range(2000002)]

for i in range(k):
    temp = int(f.readline())
    temp += m
    arr[temp] += 1

for i in range(len(arr)):
    for j in range(0,arr[i]):
        num = i - m
        print(num)

