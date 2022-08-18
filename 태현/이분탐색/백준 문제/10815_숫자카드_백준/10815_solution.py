# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)
from sys import stdin as f

f = open('testcase.txt','r')
n = int(f.readline().split()[0])
cards1 = sorted(list(map(int,f.readline().split())))
m = int(f.readline().split()[0])
cards2 = list(map(int,f.readline().split()))

# def binary_search(arr,st,en,m, target):
#     if target == arr[m]:
#         return True
#     elif st == en :
#         return False
#     elif target < arr[m]:
#         en = m - 1
#         m = (m + st) // 2
#         return binury_search(arr,st,en,m,target)
#     elif target > arr[m]:
#         st = m
#         m = (st + en) // 2
#         return binury_search(arr,st,en,m,target)

def binary_search(arr,start,end,mid,target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else :
            start = mid + 1
    return False


for card in cards2:
    if binary_search(cards1,0,len(cards1)-1,len(cards1)//2,card):
        print(1, end = ' ')
    else :
        print(0, end = ' ')