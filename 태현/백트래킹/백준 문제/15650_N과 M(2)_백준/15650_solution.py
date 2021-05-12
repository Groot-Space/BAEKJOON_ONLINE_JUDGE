from sys import stdin

nm = list(map(int,stdin.readline().split()))
n = nm[0]
m = nm[1]
arr = [i for i in range(1, n+1)]
isused = [0 for i in range(len(arr))]
rets = []
def backtrack(arr,m,k, rets, isused, i):
    if k == m:
        for j in range(len(rets)):
            if j != len(rets)-1:
                print(rets[j], end=' ')
            else :
                print(rets[j])
    else :
        for i in range(i,len(arr)):

            if isused[i] == 0:
                rets.append(arr[i])
                isused[i] = 1
                backtrack(arr,m,k+1,rets,isused, i)
                rets.pop()
                isused[i] = 0

backtrack(arr, m, 0, rets,isused, 0)