from sys import stdin as f
from copy import deepcopy
# 테스트케이스 입력
f = open('testcase.txt', 'r')
n, m = list(map(int, f.readline().split()))
#4, 2
arr = list(map(int, f.readline().split()))
arr.sort()
# 1,2,3,100
result = []
ret = []

check = [0 for i in range(len(arr))]

def solution(result,arr,ret,check):
    if len(result) == m:
        for item in result:
            print(item, end = ' ')
        print()
    else :
        for i in range(len(arr)):
            if check[i] == 0:
                result.append(arr[i])
                check[i] = 1
                solution(result,arr,ret,check)
                result.pop()
                check[i] = 0

solution(result,arr,ret,check)
