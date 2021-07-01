from sys import stdin as f
from collections import deque
from copy import deepcopy

def bfs(board, visited, dirs, start_point):
    flag = 0
    while len(start_point) > 0:
        cur = start_point.popleft()
        for d in dirs:
            y = cur[1] + d[0]
            x = cur[0] + d[1]
            if y >= 0 and y < len(board) and x >= 0 and x < len(board[0]):
                if board[y][x] == 1 and visited[y][x] != 1:
                    visited[y][x] = 1
                    flag = 1
                    start_point.append([x, y])
    return flag



f = open('testcase.txt', 'r')
t = list(map(int,f.readline().split()))[0]
for i in range(t):
    m, n, k = list(map(int,f.readline().split())) #m이 가로, n이 세로
    cabbage = [list(map(int,f.readline().split())) for j in range(k)] #x, y
    board = [[0 for j in range(m)] for l in range(n)]
    visited = deepcopy(board)
    for j in range(len(cabbage)):
        board[cabbage[j][1]][cabbage[j][0]] = 1

    dirs = ((0,0), (-1,0), (1,0), (0,-1), (0,1))
    start_point = deque()
    ans = 0
    for j in range(len(cabbage)):
        start_point.append(cabbage[j])
        ans += bfs(board, visited, dirs, start_point)
    print(ans)