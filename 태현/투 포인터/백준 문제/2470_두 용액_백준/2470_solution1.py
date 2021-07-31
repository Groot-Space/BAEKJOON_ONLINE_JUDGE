'''
이 문제를 일반적인 two point로 풀 때 문제점
1. 문제의 본질은 두 정수의 합이 가장 0에 가까운 두 정수를 구하는 것임.
2. 일반적인 two point는 arr[st] + arr[en] 과 target을 비교해가며 target보다 arr[st] + arr[en]이 적을 때 en에 +1을 하고,
그렇지 않을 때 st에 +1을 해주면서 배열을 전체 탐색하는 알고리즘임.
3. 그러나 이 문제의 경우 -의 수가 포함되면서 -99, -98, -1, 3, 8, 98 이라는 수를 예로 들 때, 답은 -98과 98인데 그 사이에 값들이 0과의 거리가 들쑥날쑥해지면서 st가 -98에
고정될 수가 없음.
4. 그래서, -관련 수가 들어오게 되면 st를 0 en을 max로 주고 검색하는 노하우가 필요함.

'''
from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
arr = list(map(int, f.readline().split()))
arr.sort()

def get_dist(arr,st,en):
    return (0 - (arr[st] + arr[en])) ** 2

def two_point(arr):
    total = float('inf')
    en = 1
    for st in range(len(arr)):

        while get_dist(arr,st,en) < total:
            en += 1
