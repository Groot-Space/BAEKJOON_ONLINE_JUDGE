from sys import stdin as f

f = open('testcase.txt', 'r')

n, m = list(map(int,f.readline().split()))
arr = []
for i in range(n):
    arr.append(int(f.readline().split()[0]))

arr.sort()

low = 1
hight = arr[-1] - arr[0]

house = [False for i in range(arr[-1])]

for home in arr:
    house[home] = True

def search(num, house):
    for i in range(0,len(house),num):
        if house[i] == False:
            return False

def bisearch(m, house):
    start = 0
    end = len(house) - 1
    ans = 0
    while m >= 0 and m <= len(house):
        m = (start + end) // 2
