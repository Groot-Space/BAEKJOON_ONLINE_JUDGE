from sys import stdin as f
from collections import deque
import sys
from bisect import bisect_left,bisect_right
# 직접 구현할 땐 while문을 쓰자 .. 시간초과 뜬다 ..
sys.setrecursionlimit(10 ** 6)
f = open('testcase.txt','r')

n = int(f.readline().split()[0])
card = list(map(int, f.readline().split()))
target_num = int(f.readline().split()[0])
target = list(map(int, f.readline().split()))

# def bi_search_low(card,target,st,mid,en):
#     if st == en:
#         return en
#     else :
#         if card[mid] >= target:
#             en = mid
#             return bi_search_low(card,target, st, (st+en) // 2, en)
#
#         else :
#             st = mid + 1
#             return bi_search_low(card,target, st, (st+en) // 2, en)
#
# def bi_search_up(card,target,st,mid,en):
#     if st == en:
#         return en
#     else :
#         if card[mid] <= target:
#             st = mid + 1
#             return bi_search_up(card,target,st, (st+en) // 2,en)
#         else:
#             en = mid
#             return bi_search_up(card,target,st, (st+en) // 2,en)

card.sort()

for i in range(len(target)):
    # low = bi_search_low(card,target[i], 0, len(card)//2 , len(card))
    # up = bi_search_up(card,target[i],0,len(card)//2,len(card))
    low = bisect_left(card, target[i])
    up = bisect_right(card, target[i])
    print(up-low, end=' ')