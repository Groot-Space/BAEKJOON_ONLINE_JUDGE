n = int(input())

isused_x = [0 for i in range(n)]
isused_diagonal_plus = [0 for i in range(2*n)]
isused_diagonal_minus = [0 for i in range(2*n)]
def solution(cur, count, n, isused_x, isused_diagnoal_plus, isused_diagnoal_minus):
    if cur == n:
        return count + 1
    else :
        for x in range(n):
            if isused_x[x] == 0 and isused_diagnoal_plus[x+cur] == 0 and isused_diagnoal_minus[x-cur+n-1] == 0:
                isused_x[x] = 1
                isused_diagnoal_plus[x+cur] = 1
                isused_diagnoal_minus[x-cur+n-1] = 1
                count = solution(cur+1, count,n,isused_x,isused_diagnoal_plus,isused_diagnoal_minus)
                isused_x[x] = 0
                isused_diagnoal_plus[x+cur] = 0
                isused_diagnoal_minus[x-cur+n-1] = 0
    return count

print(solution(0,0,n,isused_x,isused_diagonal_plus,isused_diagonal_minus))
