from sys import stdin as f
from collections import deque
from copy import deepcopy
f = open('testcase.txt','r')
lc = list(map(int,f.readline().split()))
size = lc[0]
m = lc[1]

houses = deque()
chikens = deque()

for i in range(0, size):
    tmp = list(map(int,f.readline().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            houses.append([i+1,j+1,100000]) #l,c,치킨거리
        if tmp[j] == 2:
            chikens.append([i+1,j+1])

candidates = []
arr = []
def back_track(chikens,arr,candidates, m, i):
    if len(arr) == m:
        candidates.append(deepcopy(arr))
        # return candidates
    else:
        for i in range(i, len(chikens)):
            arr.append(chikens[i])
            back_track(chikens,arr,candidates,m, i+1)
            arr.pop()
        return candidates

def dist(l1,c1,l2,c2):
    right = l1-l2
    left = c1-c2
    if right < 0:
        right *= -1
    if left < 0:
        left *= -1
    return right + left

def get_chicken_dist(houses, candidates, limit):
    ret = []
    for candidate in candidates:
        limit_candidate = candidate[:limit]
        _houses = deepcopy(houses)
        for house in _houses:
            for chiken in limit_candidate:
                tmp = dist(house[0], house[1], chiken[0], chiken[1])
                if house[2] > tmp:
                    house[2] = tmp
        _sum = 0
        for house in _houses:
            _sum += house[2]
        ret.append(_sum)
    return ret

# def get_min_dist(ret):
#     mn = 10000000000
#     for i in range(len(ret)):
#         total = 0
#         for j in range(len(ret[i])):
#             total += ret[i][j][2]
#         if total < mn:
#             mn = total
#     return mn

ans = 10000000000000
candidates = back_track(chikens,arr,candidates,m,0)
for i in range(1,m+1):
    _ans = min(get_chicken_dist(houses, candidates,i))
    if ans > _ans:
        ans = _ans

print(ans)