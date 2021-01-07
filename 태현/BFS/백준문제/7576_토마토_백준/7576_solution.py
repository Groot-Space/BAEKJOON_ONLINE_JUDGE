from sys import stdin as f
import collections
def dfs(mp, dist, queue, max_count, wh):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = len(queue)
    ans = 0
    while len(queue) != 0:
        cur = queue.popleft()
        for dir in dirs:
            y = cur[0] + dir[0]
            x = cur[1] + dir[1]
            if y >= 0 and y < wh[1] and x >= 0 and x < wh[0] and mp[y][x] == '0' and dist[y][x] == -1:
                queue.append([y, x])
                dist[y][x] = dist[cur[0]][cur[1]] + 1
                count += 1
                if dist[y][x] > ans:
                    ans = dist[y][x]

    # print(max_count, count)
    if count < max_count:
        return -1
    else:
        return ans


f = open('testcase.txt', 'r')
wh = list(map(int,f.readline().split()))

dist = [[-1 for i in range(wh[0])] for j in range(wh[1])]

mp = [f.readline().split() for i in range(wh[1])]

queue = collections.deque()
_temp_num = 0

for i in range(wh[1]):
    for j in range(wh[0]):
        if mp[i][j] == '1':
            queue.append([i,j])
            dist[i][j] = 0
        elif mp[i][j] == '-1':
            _temp_num += 1

max_count = wh[0] * wh[1] - _temp_num

if max_count == len(queue):
    print(0)
else :
    ans = dfs(mp, dist, queue, max_count, wh)
    print(ans)