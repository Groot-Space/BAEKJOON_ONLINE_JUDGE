from sys import stdin as f
from copy import deepcopy
f = open('testcase.txt', 'r')

k = int(f.readline().split()[0])
is_used = [list(map(int, f.readline().split())) for i in range(k)]
is_used_diagonal_plus = [0 for i in range(2*k)] # 우상하 확인
is_used_diagonal_minus = [0 for i in range(2*k)] # 좌상하 확인
cur = (0,0)
count = 0

def solution(cur, count, k, is_used, isused_diagonal_plus, is_used_diagnoal_minus):
    for i in range(k):
        for j in range()


    if is_used[cur[0]][cur[1]] == 1:
        if cur[1] == k-1:
            if cur[0] == k-1:
                return count
            else :
                cur[0] += 1
                return solution(cur, count, k, is_used, isused_diagonal_plus, is_used_diagnoal_minus)
        else :
            cur[1] += 1
            return solution(cur, count, k, is_used, isused_diagonal_plus, is_used_diagnoal_minus)

    else :





