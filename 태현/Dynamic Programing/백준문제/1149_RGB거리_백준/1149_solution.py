from sys import stdin as f
import sys
sys.setrecursionlimit(100000)
f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
rgb = []
d = [[0, 0, 0] for i in range(n)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(d)
for i in range(n):
    rgb.append(list(map(int,f.readline().split())))
# rgb = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]

def dynamic(rgb, d, n):
    if n == 0:
        d[n][0] = rgb[n][0]
        d[n][1] = rgb[n][1]
        d[n][2] = rgb[n][2]
        return d
    else :
        temp = dynamic(rgb,d,n-1)
        d[n][0] = min(temp[n-1][1], temp[n-1][2]) + rgb[n][0]
        d[n][1] = min(temp[n-1][0], temp[n-1][2]) + rgb[n][1]
        d[n][2] = min(temp[n-1][0], temp[n-1][1]) + rgb[n][2]
        return d

ans_arr = dynamic(rgb,d,n-1)
ans = min(ans_arr[len(ans_arr)-1][0],ans_arr[len(ans_arr)-1][1],ans_arr[len(ans_arr)-1][2])
print(ans)