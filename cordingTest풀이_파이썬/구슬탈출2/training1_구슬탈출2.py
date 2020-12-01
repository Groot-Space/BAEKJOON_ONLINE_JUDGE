# 공의 위치를 확인-> 정보저장(공위치, 이동횟수)-> bfs구현 -> 이동 -> 결과출력
# input과정
line = input().split()
line_len = len(line)
n = int(line[0])
m = int(line[1])
Map = [list(input()) for i in range(n)]

# 정보저장 틀(클래스로 구현)
q = []
check = [[[[False]*m for l in range(n)] for j in range(m)] for k in range(n)]

class info:
    def __init__(self, R, B, C):
            self.R = R
            self.B = B
            self.C = C

# 정보저장
_temp = [0, 0, 0, 0, 0]
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'R':
            _temp[0] = i
            _temp[1] = j
        if Map[i][j] == 'B':
            _temp[2] = i
            _temp[3] = j

q.append(info([_temp[0], _temp[1]], [_temp[2], _temp[3]], 0))
check[_temp[0]][_temp[1]][_temp[2]][_temp[3]] = True

# bfs
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def move(x, y, i, Map):
    move_suc = 0
    while Map[x + i[0]][y + i[1]] != '#' and Map[x + i[0]][y + i[1]] != 'O':
        x += i[0]
        y += i[1]
        move_suc += 1
    return x, y, move_suc


def bfs(Map, q, dir, check):
    while(len(q) != 0):
        cur = q[0]
        q = q[1:]

        for i in dir:
            count = cur.C
            r_x = cur.R[0]
            r_y = cur.R[1]
            b_x = cur.B[0]
            b_y = cur.B[1]

            if count >= 10:
                return -1


            #이동 1번
            r_x, r_y, r_move_suc = move(r_x, r_y, i, Map)
            b_x, b_y, b_move_suc = move(b_x, b_y, i, Map)

            # r의 현재 위치가 '#'인지 확인
            if Map[b_x + i[0]][b_y + i[1]] == 'O':
                continue

            if Map[r_x + i[0]][r_y + i[1]] == 'O':
                return count+1

            if r_x == b_x and r_y == b_y:
                if r_move_suc < b_move_suc:
                    b_x = b_x - i[0]
                    b_y = b_y - i[1]
                else:
                    r_x = r_x - i[0]
                    r_y = r_y - i[1]


            if check[r_x][r_y][b_x][b_y] == True :
                continue
            else:
                check[r_x][r_y][b_x][b_y] = True
                q.append(info([r_x, r_y], [b_x, b_y], count+1))

    return -1

# 메인 실행
print(bfs(Map, q, dir, check))
