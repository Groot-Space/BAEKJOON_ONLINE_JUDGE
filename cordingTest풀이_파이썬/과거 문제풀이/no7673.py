import numpy as np

T_TIMES = 0
F_TIMES = 1
R = 0
C = 1
UP = 0
LEFT = 1
FAIL = -1
UNVISITED = -2
DIRS = np.array([[-1,0][0,-1]])
t = 0
f = 0
test_case = int(input())


for i in range(0, test_case+1):
    nSize = int(input())
    map = np.zeros(nSize, nSize, 2)
    temp = np.array([0, 0])
    for row in range(0, nSize):
        _s = input()
        s = _s.split()
        for col in range(0, nSize):
            val = int(s[col])
            if val == 0:
                map[row][col][T_TIMES] = FAIL
                continue

            else:
                while(True):
                    if val % 2 == 0 :
                        val /= 2
                        map[row][col][T_TIMES] += 1
                    elif val % 5 == 0:
                        val /= 5
                        map[row][col][F_TIMES] += 1
                    else:
                        break

        flag = 0
        for dir in range(UP, LEFT+1):
            prevRow = row + DIRS[dir][R]
            prevCol = col + DIRS[dir][C]
            if prevRow >= 0 and prevRow < nSize and prevCol >= 0 and prevCol < nSize:
                if map[prevRow][prevCol][T_TIMES] == FAIL:
                    continue
                if flag == 0:
                    flag += 1
                    temp[T_TIMES] = map[prevRow][prevCol][T_TIMES] + map[row][col][T_TIMES]
                    temp[T_TIMES] = map[prevRow][prevCol][F_TIMES] + map[row][col][F_TIMES]

                else :
                    flag += 1
                    prev = min(temp[T_TIMES], temp[F_TIMES])
                    now = min(map[prevRow][prevCol][T_TIMES]+ map[row][col][T_TIMES], map[prevRow][prevCol][F_TIMES] + map[row][col][F_TIMES])

                    if prev < now :
                        map[row][col][T_TIMES] = temp[T_TIMES]
                        map[row][col][F_TIMES] = temp[F_TIMES]
                    else :
                        map[row][col][T_TIMES] += map[prevRow][prevCol][T_TIMES]
                        map[row][col][F_TIMES] += map[prevRow][prevCol][F_TIMES]

        if flag == 0 and row != 0 and col != 0 :
            map[row][col][T_TIMES] = FAIL
        elif row != 0 and col != 0 and flag == 1:
            map[row][col][T_TIMES] = temp[T_TIMES]
            map[row][col][F_TIMES] = temp[F_TIMES]


    ret = min(map[nSize - 1][nSize - 1][T_TIMES], map[nSize - 1][nSize - 1][F_TIMES])

    print("# " + ret)
