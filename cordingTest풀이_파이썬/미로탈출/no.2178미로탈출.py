Input = input()
n, m = map(int, Input.split())

Map = [list(input()) for i in range(n)]

class info:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

_info = info(0,0, 1)

dir = [[-1,0],[1,0],[0,-1],[0,1]]
q = []
q.append(_info)
check = [[False]*m for _ in range(n)]
check[0][0] = True

def bfs(Map, q, dir, n, m):
    while len(q) != 0:
        cur = q[0]
        q = q[1:]

        for i in dir:
            c_x = cur.x + i[0]
            c_y = cur.y + i[1]
            count = cur.c


            if c_x == -1 or c_y == -1 or c_x == n or c_y == m:
                continue

            if Map[c_x][c_y] == '0':
                continue

            elif c_x == n-1 and c_y == m-1:
                return count+1

            elif check[c_x][c_y] == True:
                continue

            else :
                check[c_x][c_y] = True
                q.append(info(c_x, c_y, count+1))

print(bfs(Map, q, dir, n, m))