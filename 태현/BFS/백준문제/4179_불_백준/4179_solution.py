from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')
r, c = list(map(int, f.readline().split()))

mp = []
for i in range(r):
    tmp = str(f.readline().rstrip())
    tmp2 = []
    for j in tmp:
        tmp2.append(j)
    mp.append(tmp2)

visited = [[0 for i in range(c)] for j in range(r)]

J_queue = deque()
F_queue = deque()
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for i in range(r):
    for j in range(c):
        if mp[i][j] == 'J':
            J_queue.append([i,j])
            visited[i][j] = 1
        elif mp[i][j] == 'F':
            F_queue.append([i,j])
            visited[i][j] = -1

def dfs(J_queue, F_queue, dirs, visited,r , c):
    while len(J_queue) != 0:
        J = J_queue.popleft()
        F = F_queue.popleft()
        for dir in dirs:
            if visited[J[0]][J[1]] != -1:
                J_y = J[0] + dir[0]
                J_x = J[1] + dir[1]
                F_y = F[0] + dir[0]
                F_x = F[1] + dir[1]
                if mp[J_y][J_x] != '#' and visited[J_y][J_y] == 0 and J_y < r and J_x < c:
                    visited[J_y][J_x] = visited[J[0]][J[1]] + 1
                    J_queue.append([J_y, J_x])

                    if J_y == 0 or J_y == r-1 or J_x == 0 or J_x == c-1:
                        return visited[J_y][J_x]

                if mp[F_y][F_x] != '#' and F_y < r and F_x < c:
                    visited[F_y][F_x] = -1
                    F_queue.append([F_y,F_x])

    return 'IMPOSSIBLE'

print(dfs(J_queue, F_queue, dirs, visited, r, c))
# print(mp)