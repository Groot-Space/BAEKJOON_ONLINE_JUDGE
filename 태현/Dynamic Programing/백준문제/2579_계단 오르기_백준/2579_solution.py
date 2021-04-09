from collections import deque

f = open('testcase.txt', 'r')

stair_num = int(f.readline().split()[0])
stair = []

for i in range(stair_num):
    stair.append(int(f.readline().split()[0]))

D = [[0,0] for i in range(stair_num)]
# [해당 계단을 밟았을 때 최대 값, 해당 계단을 밟지 않았을 때 최대 값

ans = 0

if stair_num >= 3:
    D[0][0] = stair[0] #1번 째 계단을 밟았을 때 최대 값
    D[0][1] = stair[0]
    D[1][0] = stair[1] #2번 째 계단을 밟았을 때 최대 값
    D[1][1] = stair[1] + stair[0]
    for i in range(2, stair_num):
        D[i][0] = stair[i] + max([D[i - 2][0], D[i - 2][1]])
        D[i][1] = stair[i] + D[i - 1][0]

    print(max([D[stair_num - 1][0], D[stair_num - 1][1]]))

else :
    for i in range(stair_num):
        ans += stair[i]
    print(ans)