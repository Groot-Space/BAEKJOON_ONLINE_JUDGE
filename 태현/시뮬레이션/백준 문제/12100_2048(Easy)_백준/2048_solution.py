from sys import stdin as f
from copy import deepcopy
f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
mp = []
for i in range(n):
    mp.append(list(map(int,f.readline().split())))

'''
0도 = 좌, 0
90도 = 상, 1
180도 = 우, 2
270도 = 하, 3
'''
def tilt(mp):
    new_mp = [[0 for i in range(len(mp[0]))] for j in range(len(mp))]
    for i in range(len(mp)):
        _idx = 0
        for j in range(len(mp)):
            if mp[i][j] != 0:
                if new_mp[i][_idx] == 0:
                    new_mp[i][_idx] = mp[i][j]
                elif new_mp[i][_idx] != 0 and new_mp[i][_idx] == mp[i][j]:
                    new_mp[i][_idx] += mp[i][j]
                    _idx += 1
                else :
                    _idx += 1
                    new_mp[i][_idx] = mp[i][j]
    return new_mp

def rotation(a, mp):
    if a == 0:
        return mp
    new_mp = [[0 for i in range(len(mp[0]))] for j in range(len(mp))]
    if a == 1:
        for i in range(len(new_mp)):
            idx = 0
            for j in range(len(new_mp)-1, -1 , -1):
                new_mp[i][idx] = mp[j][i]
                idx += 1
        return new_mp
    if a == 2:
        l_idx = len(mp) - 1
        for i in range(len(mp)):
            c_idx = len(mp[0]) - 1
            for j in range(len(mp[0])):
                new_mp[i][j] = mp[l_idx][c_idx]
                c_idx -= 1
            l_idx -= 1
        return new_mp
    if a == 3:
        c_idx = len(mp[0]) - 1
        for i in range(len(mp)):
            l_idx = 0
            for j in range(len(mp[0])):
                new_mp[i][j] = mp[l_idx][c_idx]
                l_idx += 1
            c_idx -= 1
        return new_mp

def get_max(mp):
    mx = 0
    for i in range(len(mp)):
        _temp = max(mp[i])
        if _temp > mx:
            mx = _temp
    return mx

k = 5
angle = []
candidate = []

def combination(k,angle,candidate):
    if len(angle) == k:
        candidate.append(deepcopy(angle))
        return candidate

    else:
        for i in range(0,4):
            angle.append(i)
            candidate = combination(k, angle, candidate)
            angle.pop()
        return candidate

candidate = combination(k,angle,candidate)
# for i in candidate:
#     print(i)
#
# candidates = [[3, 3, 1, 1, 3]]
mx = 0
for i in candidate:
    _mp = deepcopy(mp)
    for j in i:
        _mp = rotation(j, _mp)
        _mp = tilt(_mp)
    _mx = get_max(_mp)
    if mx < _mx:
        mx = _mx

print(mx)