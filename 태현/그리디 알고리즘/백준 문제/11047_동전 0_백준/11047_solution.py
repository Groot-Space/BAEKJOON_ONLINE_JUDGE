from sys import stdin as f

f = open('testcase.txt','r')
n, k = list(map(int,f.readline().split()))
coin = [int(f.readline().split()[0]) for i in range(n)]
count = 0

for i in range(n-1,-1,-1):
    count += k // coin[i]
    k = k % coin[i]
print(count)