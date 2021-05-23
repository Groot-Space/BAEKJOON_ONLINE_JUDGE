import sys
limit_number = 10**6
sys.setrecursionlimit(limit_number)

n = int(input())
arr = [0 for i in range(n+1)]
arr[0] = 1
arr[1] = 2

def dynamic(arr,n):
    if n <= 1:
        return arr
    else:
        arr = dynamic(arr,n-1)
        arr[n] = (arr[n-1] + arr[n-2]) % 10007
        return arr

if n <= 2:
    print(arr[n-1])
else :
    print(dynamic(arr,n-1)[n-1])

