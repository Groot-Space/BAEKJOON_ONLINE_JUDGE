from sys import stdin
from collections import deque

input = stdin.readline
#입력한 한개의 라인을 받아옴, 개행문자까지 받아옴.
n,m = map(int, input().split())
#split()는 개행문자를 생략하면서 요소 한개를 가져오는 듯.
#map함수는 리스트 요소들의 자료형을 바꿀 때 써줌.
a = [list(input()) for _ in range(n)]
#strip()는 input()옆에 붙여도 안붙여도 상관없음. 공백 제거 역할임. 2차원배열로 만드는 역할의 코드.
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
#4차원배열 선언, False가 총 5개, 방문을 저장할 때 사용함.
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()
#*큐 사용, 어디에 쓰는지는 잘 모르겠음

def init():#구조체느낌, 레드와 블루의 위치를 1차원 리스트로 저장,
    _rx, _ry, _bx, _by = [0] * 4
    #각 요소를 _rx = 0 형태로 선언, 리스트아닌 것에 주의
    for i in range(n):
        #맵의 가로를 탐색
        for j in range(m):
            #맵의 세로를 탐색
            if a[i][j] =='R':
                #맵을 돌면서 빨간 공을 발견하면
                _rx, _ry = i, j
                # 저장
            elif a[i][j] == 'B':
                _bx, by = i, j
    q.append((_rx,_ry,_bx,_by, 1))
    #튜플 형태로 큐에 저장, 0은 이동 횟수인가봄.
    check[_rx][_ry][_bx][_by] = True
    #현재 위치는 True로 지정해줌

def move(_x, _y, _dx, _dy): #현재위치의 x, y, (dx, dy)상하좌우 움직이는 좌표, 이동거리)
    count = 0
    while a[_x + _dx][_y + _dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        count += 1
    return _x, _y, count

def bfs():
    init()
    while q: #큐의 모든 요소를 빼내옴.
        rx, ry, bx, by, d = q.popleft()
        # 빼내온 요소를 위와 같이 지정
        if d > 10:
            # 꺽어진 횟수가 10회 이상일 경우 탈출.
            break
        for i in range(len(dx)):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            #반환값은 벽에 부딪히기 전까지 펼처진(bfs이기 때문에 펼처지다로 표기함)후의 좌표 값과 이동거리.
            #혹은 'O'이 될 대까지 펼처짐.
            if a[nbx][nby] == 'O':
                continue
                #파란 색이 O에 들어가면 밑에 안보고 다시 for문을 돌림.
            if a[nrx][nry] == 'O':
                print(d)
                #빨간 색이 O에 들어가면 요번 턴 움직인 것 까지 1 더해서 리턴
                return
            if nrx == nbx and nry == nby:
                #만약 빨간 공과 파란 공이 같은 위치에 있을 경우
                if rc > bc:
                    #빨간 공이 더 멀리 있었으면
                    nrx, nry = nrx - dx[i], nry - dy[i]
                    #빨간공을 방향에서 한칸 앞으로...
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nrx][nry][nbx][nby]:
                #만약에 방문한 적이 없으면
                check[nrx][nry][nbx][nby] = True
                #방문처리 한 후에
                q.append((nrx, nry, nbx, nby, d+1))
                #이동횟수 +1을 해주고 저장
    print(-1)

bfs()

