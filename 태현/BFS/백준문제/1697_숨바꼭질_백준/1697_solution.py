from sys import stdin
from collections import deque
from copy import deepcopy

n, k = list(map(int, stdin.readline().split()))

board = [-1 for i in range(100001)]

board[n] = 0
queue = deque()
queue.append(n)
dist = deepcopy(board)
def bfs(board,queue, dist):
    while len(queue) != 0:
        cur = queue.popleft()
        for i in range(3):
            if i == 0:
                new_x = cur -1
            elif i == 1:
                new_x = cur + 1
            else:
                new_x = cur * 2

            if new_x >= 0 and new_x < len(board):
                _tmp = dist[cur] + 1
                if dist[new_x] == -1 or dist[new_x] > _tmp:
                    dist[new_x] = _tmp
                    queue.append(new_x)


bfs(board,queue,dist)
print(dist[k])