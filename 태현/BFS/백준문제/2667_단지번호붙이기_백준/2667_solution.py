from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
mp = []
for i in range(n):
    tmp = f.readline().split()[0]
    tmp2 = []
    for j in range(len(tmp)):
        tmp2.append(tmp[j])
    mp.append(tmp2)

# print(mp)

start_points = []
for i in range(len(mp)):
    for j in range(len(mp[0])):
        if mp[i][j] == '1':
            start_points.append((i,j))
# print(start_points)

counts = []
visited = [[0 for i in range(len(mp[0]))] for j in range(len(mp))]
stack = deque()

def oob(new_y, new_x, mp):
    if new_y < len(mp) and new_y >= 0 and new_x < len(mp[0]) and new_x >= 0:
        return True
    else :
        return False

def dfs(visited, stack, mp, idx):
    dirs = ((0,0), (1,0), (0,1), (-1,0), (0,-1))
    count = 0
    while stack:
        cur = stack.pop()

        for dir in dirs:
            new_y = cur[0] + dir[0]
            new_x = cur[1] + dir[1]
            if oob(new_y, new_x, mp):
                if mp[new_y][new_x] == '1' and visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = idx
                    stack.append((new_y,new_x))
                    count += 1
    return count

for i in range(len(start_points)):
    # print()
    if visited[start_points[i][0]][start_points[i][1]] == 0:
        stack.append(start_points[i])
        tmp = dfs(visited, stack, mp, i+1)
        if tmp != 0:
            counts.append(tmp)
counts.sort()
print(len(counts))
for i in range(len(counts)):
    print(counts[i])
