from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

t = int(f.readline().split()[0])


def cycle_check_dfs(board, stack,visited, i, n):
    while len(stack) != 0:
        new_cur = board[stack.pop()]
        if visited[new_cur] == 0:
            visited[new_cur] = i
            stack.append(new_cur)
        elif visited[new_cur] == i:
            while visited[new_cur] != -1:
                visited[new_cur] = -1
                new_cur = board[new_cur]
                n -= 1
    return n

while t > 0:
    n = int(f.readline().split()[0])
    board = [0]
    board.extend(list(map(int,f.readline().split())))
    visited = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if visited[i] != -1:
            visited[i] = i
            n = cycle_check_dfs(board, deque([i]), visited, i, n)
    print(n)
    t -= 1