from collections import deque

def _rotataion(sticker):
    _n = len(sticker)
    _m = len(sticker[0])
    rotated = [['0' for i in range(_n)] for j in range(_m)]
    rotated_x = _n-1
    for k in range(_n):
        for l in range(_m):
            rotated[l][rotated_x] = sticker[k][l]
        rotated_x -= 1
    return rotated

def check_size(board, y,x):
    if len(board) < y or len(board[0]) < x:
        return True
    else :
        return False

def solution(board, stickers, count):
    if len(stickers) == 0:
        return [board, count]

    sticker, angle = stickers.popleft()
    while check_size(board, len(sticker), len(sticker[0])) and angle < 4:
        sticker = _rotataion(sticker)
        angle += 1

    if angle == 4:
        board,count = solution(board,stickers, count)
        return [board,count]
    flag = 0
    for i in range(len(board) - len(sticker) + 1):
        stride_y = i
        for j in range(len(board[0])- len(sticker[0]) + 1):
            stride_x = j
            flag = 0
            for n in range(len(sticker)):
                if flag == 1:
                    break
                for m in range(len(sticker[0])):
                    if flag == 1:
                        break
                    elif sticker[n][m] == '1':
                        if board[n+stride_y][m+stride_x] == '1':
                            flag = 1
                            break

            if flag == 0:
                for o in range(len(sticker)):
                    for p in range(len(sticker[0])):
                        if sticker[o][p] == '1' and board[o+stride_y][p+stride_x] == '0':
                            board[o+stride_y][p+stride_x] = '1'
                            count += 1

                board,count = solution(board, stickers, count)
                return [board, count]

    if flag == 1:
        sticker = _rotataion(sticker)
        stickers.appendleft([sticker, angle + 1])
        return solution(board, stickers, count)



f = open('testcase.txt', 'r')
n, m, k = list(map(int, f.readline().split()))
#세로, 가로, 스티커 갯수
board = [['0' for i in range(m)] for j in range(n)]
stickers = deque()

for i in range(k):
    s_n, s_m = list(map(int, f.readline().split()))
    sticker = [f.readline().split() for j in range(s_n)]
    stickers.append([sticker,0])

count = 0
board, count = solution(board, stickers, count)
print(count)
'''
1. 스티커가 board 안에 들어가는지 확인.
    안들어가면 회전 -> 3번 회전해서 안들어가면 버림
2. 이중 for문 stride를 하면서 board와 sticker의 1이 겹치는 부분이 있는지 확인. 
    board범위를 벗어나는지 확인
        벗어나면 continue
    있으면 continue하고 다시 stride
    없으면 board에 마킹
3. 2번 수행 후 못붙였으면, 회전
    board범위를 벗어나는지 확인
    벗어나면 다시 회전 - 3회 회전 후에도 벗어나면 스티커 버림.
    안벗어나면 다시 2번 반복
'''