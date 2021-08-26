from sys import stdin as f
from collections import deque

# f = open('testcase.txt', 'r')

# n = int(f.readline().split()[0])
n = 2
table = [[[float('inf'),0],[float('inf'),0],[float('inf'),0]] for i in range(n+1)]

# print(table[0][0][0])
table[0][0][0] = n
table[0][1][0] = n
table[0][2][0] = n
#
def table_print(i, j, arr, ret):
    if i >= 0 :
        ret.appendleft(arr[i][j][0])
        idx = arr[i][j][1]

        table_print(i-1, idx, arr,ret)
    # else :
    #     return ret

def dynamic(arr):
    flag = 0
    _i = 0
    _j = 0
    for i in range(1,len(arr)):
        if flag == 1:
            _i = i-1
            break

        for j in range(len(arr[i])):
            if arr[i-1][j][0] % 3 == 0:
                tmp = arr[i-1][j][0] // 3
                if tmp < arr[i][0][0]:
                    arr[i][0][0] = tmp
                    arr[i][0][1] = j

            if arr[i-1][j][0] % 2 == 0:
                tmp = arr[i-1][j][0] // 2
                if tmp < arr[i][1][0] :
                    arr[i][1][0] = tmp
                    arr[i][1][1] = j

            tmp = arr[i-1][j][0] - 1
            if tmp < arr[i][2][0]:
                arr[i][2][0] = tmp
                arr[i][2][1] = j

            if arr[i][j][0] == 1:
                flag = 1
                _j = j
                break

    ret = deque()
    print(_i)
    table_print(_i, _j, arr, ret)
    # print(ret)
    for i in range(len(ret)):
        print(ret[i], end = ' ')



