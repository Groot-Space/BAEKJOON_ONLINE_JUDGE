from sys import stdin as f
from collections import deque
from copy import deepcopy
#불 bfs 따로, 지훈이 bfs 따로


f = open('testcase.txt', 'r')
r, c = list(map(int, f.readline().split()))

mp = []
for i in range(r):
    tmp = str(f.readline().rstrip())
    tmp2 = []
    for j in tmp:
        tmp2.append(j)
    mp.append(tmp2)

f_visited = [[0 for i in range(c)] for j in range(r)]
j_visited = deepcopy(f_visited)

J_queue = deque()
F_queue = deque()
dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
for i in range(r):
    for j in range(c):
        if mp[i][j] == 'J':
            J_queue.append([i,j])
            j_visited[i][j] = 1
        elif mp[i][j] == 'F':
            F_queue.append([i,j])
            f_visited[i][j] = 1

def f_dfs(F_queue, dirs, visited, r, c):
    while len(F_queue) != 0:
        F = F_queue.popleft()
        for dir in dirs:
            F_y = F[0] + dir[0]
            F_x = F[1] + dir[1]
            if F_y < r and F_x < c and F_y >= 0 and F_x >= 0:
                if mp[F_y][F_x] != '#' and visited[F_y][F_x] == 0:
                    visited[F_y][F_x] = visited[F[0]][F[1]] + 1
                    F_queue.append([F_y, F_x])

def j_dfs(J_queue, dirs, j_visited,f_visited, r , c):
    while len(J_queue) != 0:
        J = J_queue.popleft()
        for dir in dirs:
            J_y = J[0] + dir[0]
            J_x = J[1] + dir[1]
            if mp[J_y][J_x] != '#' and J_y < r and J_x < c and J_y > 0 and J_x > 0:
                tmp = j_visited[J[0]][J[1]] + 1
                if tmp < f_visited[J_y][J_x] or f_visited[J_y][J_x] == 0 and j_visited[J_y][J_x] == 0:
                    j_visited[J_y][J_x] = tmp
                    J_queue.append([J_y, J_x])
                    if J_y == 0 or J_y == r-1 or J_x == 0 or J_x == c-1:
                        return j_visited[J_y][J_x]

    return 'IMPOSSIBLE'


f_dfs(F_queue,dirs,f_visited,r,c)
print(j_dfs(J_queue, dirs, j_visited, f_visited, r, c))