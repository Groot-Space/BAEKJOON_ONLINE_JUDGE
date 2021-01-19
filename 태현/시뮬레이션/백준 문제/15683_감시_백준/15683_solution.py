from collections import deque
import copy
class cctv:
    def __init__(self,detect,y,x):
        self.detect = detect
        self.x = x
        self.y = y

def bfs(mp,queue,dirs_set,visited, count,max_count):
    if len(queue) == 0:
        if count > max_count:
            return count
        else:
            return max_count
    else :
        ctv = queue.popleft()
        x = ctv.x
        y = ctv.y
        dirs = ctv.detect
        visited[y][x] = 1
        for dir in dirs:
            _queue = copy.deepcopy(queue)
            _visited = copy.deepcopy(visited)
            _count = count
            for di in dir:
                new_y = y + dirs_set[di][0]
                new_x = x + dirs_set[di][1]
                while True:
                    if new_y < 0 or new_x < 0 or new_y >= n or new_x >= m:
                        break

                    elif mp[new_y][new_x] == '6':
                        break

                    else :
                        if _visited[new_y][new_x] == 0 and mp[new_y][new_x] == '0':
                            _visited[new_y][new_x] = 1
                            _count += 1
                        new_y += dirs_set[di][0]
                        new_x += dirs_set[di][1]

            max_count = bfs(mp,_queue,dirs_set,_visited,_count,max_count)
        return max_count


f = open('testcase.txt', 'r')
n, m = list(map(int,f.readline().split()))
mp = [f.readline().split() for i in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
dirs_set = [(-1,0), (1,0), (0,-1), (0,1)] # 상 하 좌 우

cctv_detect = [[[0],[1],[2],[3]], [[2,3],[0,1]], [[0,3],[1,2], [0,2], [1,3]], [[0,2,3],[1,2,3],[0,3,1],[2,0,1]] , [[0,1,2,3]]]
# cctv_one = [[상],[하],[좌],[우]]
# cctv_two = [[좌, 우] , [상,하]
# cctv_three = [[상,우],[하,좌],[상,좌],[하,우]]
# cctv_four = [[상,좌,우],[하,좌,우], [상,우,하],[좌,우,하]]
# cctv_five = [[상,하,좌,우]]

queue = deque()
total_zero = 0
for i in range(n):
    for j in range(m):
        if mp[i][j] == '0':
            total_zero += 1
            continue
        elif mp[i][j] == '1':
            queue.append(cctv(cctv_detect[0],i,j))
            continue
        elif mp[i][j] == '2':
            queue.append(cctv(cctv_detect[1],i,j))
            continue
        elif mp[i][j] == '3':
            queue.append(cctv(cctv_detect[2],i,j))
            continue
        elif mp[i][j] == '4':
            queue.append(cctv(cctv_detect[3],i,j))
            continue
        elif mp[i][j] == '5':
            queue.append(cctv(cctv_detect[4],i,j))
            continue
count = 0
max_count = 0
max_count = bfs(mp,queue,dirs_set,visited, count,max_count)
print(total_zero - max_count)