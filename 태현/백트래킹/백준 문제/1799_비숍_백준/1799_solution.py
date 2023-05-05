from sys import stdin as f
from copy import deepcopy

#테스트케이스 읽어옴
f = open('testcase.txt', 'r')

#k 값 받기
k = int(f.readline().split()[0])

#map 받기
board = []
for i in range(k):
    board.append(list(map(int, f.readline().split())))

#대각선 및 비숍 체크 리스트 만들기
plus = [0 for i in range(k*2)]
minus = [0 for i in range(k*2)]
check = [[0 for i in range(k)] for j in range(k)]

result = 0
def solution(_y, _x, cur, count, k, plus, minus,result):
    if cur + 1 == k:
        return count
    else :
        for y in range(_y, k):
            for x in range(_x,k):
                if board[y][x] == 1 and plus[y+x] == 0 and minus[y-x+k-1] == 0 and check[y][x] == 0:
                    plus[y+x] = 1
                    minus[y-x+k-1] = 1
                    check[y][x] = 1
                    count += 1
                    _temp = solution(x+1,cur,count,k,plus,minus,result)
                    if result < _temp:
                        result = _temp
                    _x -= 1
                    plus[y+x] = 0
                    minus[y-x+k-1] = 0
                    check[y][x] = 0
                    count -= 1
        cur += 1
    return result

solution(0,0,0,k,plus,minus,result)
print(result)
