from sys import stdin as f
from collections import deque
f = open('testcase.txt', 'r')

class dice:
    def __init__(self):
        self.wide = deque([0,0,0,0])
        self.left = 0
        self.right = 0
        self.down = 0
        self.top = 2

    def print_top(self):
        print(self.wide[self.top])

    def move_east(self):
        tmp1 = self.wide[0]
        tmp2 = self.wide[2]
        self.wide[0] = self.right
        self.wide[2] = self.left
        self.left = tmp1
        self.right = tmp2

    def move_west(self):
        tmp1 = self.wide[0]
        tmp2 = self.wide[2]
        self.wide[0] = self.left
        self.wide[2] = self.right
        self.left = tmp2
        self.right = tmp1

    def move_south(self):
        tmp = self.wide.popleft()
        self.wide.append(tmp)

    def move_north(self):
        tmp = self.wide.pop()
        self.wide.appendleft(tmp)

    def dice_append(self, a):
        self.wide[self.down] = a

def check_leng_board(board, y,x):
    if y < len(board) and x < len(board[0]) and y >= 0 and x >= 0:
        return True
    else :
        return False

dice = dice()
n, m, y, x, k = list(map(int, f.readline().split()))
arr = deque()
board = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    tmp = list(map(int,f.readline().split()))
    for j in range(len(tmp)):
        board[i][j] = tmp[j]

dirs = list(map(int,f.readline().split()))
# dice.dice_append(board[y][x])
# board[y][x] = 0
for i in range(len(dirs)):
    if dirs[i] == 1:
        if check_leng_board(board, y, x+1):
            dice.move_east()
            x += 1
            if board[y][x] != 0:
                dice.dice_append(board[y][x])
                board[y][x] = 0
            else :
                board[y][x] = dice.wide[0]
            dice.print_top()

    elif dirs[i] == 2:
        if check_leng_board(board, y, x-1):
            dice.move_west()
            x -= 1
            if board[y][x] != 0:
                dice.dice_append(board[y][x])
                board[y][x] = 0
            else :
                board[y][x] = dice.wide[0]
            dice.print_top()

    elif dirs[i] == 3:
        if check_leng_board(board,y-1, x):
            dice.move_north()
            y -= 1
            if board[y][x] != 0:
                dice.dice_append(board[y][x])
                board[y][x] = 0
            else :
                board[y][x] = dice.wide[0]
            dice.print_top()

    elif dirs[i] == 4:
        if check_leng_board(board, y+1, x):
            dice.move_south()
            y += 1
            if board[y][x] != 0:
                dice.dice_append(board[y][x])
                board[y][x] = 0
            else :
                board[y][x] = dice.wide[0]
            dice.print_top()
