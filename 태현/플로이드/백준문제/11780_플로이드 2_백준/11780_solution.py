from sys import stdin as f
from collections import deque

f = open('testcase_플로이드 2.txt', 'r')

n = int(f.readline().split()[0])
m = int(f.readline().split()[0])

board = [[float("inf") for j in range(n+1)] for i in range(n+1)]
path = [[0 for i in range(n+1)] for j in range(n+1)]
# print(board) [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

low_count = 0

def print_board(board):
    for i in range(1,len(board)):
        for j in range(1, len(board)):
            print(board[i][j], end = ' ')
        print()

while low_count < m:
    start, end, weight = list(map(int, f.readline().split()))
    if board[start][end] > weight:
        board[start][end] = weight
        path[start][end] = end
    low_count += 1

for i in range(1,n+1):
    for j in range(1,n+1): # j -> l
        for l in range(1,n+1):
            if j == l:
                continue
            tmp = board[j][i] + board[i][l]
            if tmp < board[j][l]:
                board[j][l] = tmp
                path[j][l] = path[j][i]

for i in range(1,len(board)):
    for j in range(1,len(board)):
        if board[i][j] == float('inf'):
            print(0, end=' ')
        else :
            print(board[i][j], end=' ')
    print()

for i in range(1, len(board)):
    for j in range(1, len(board)):
        if board[i][j] == float('inf'):
            print(0)
        else :
            tmp = deque()
            start = i
            tmp.append(start)
            while start != j:
                tmp.append(path[start][j])
                start = path[start][j]

            print(len(tmp), end = ' ')
            for k in range(len(tmp)):
                print(tmp[k], end = ' ')
            print()