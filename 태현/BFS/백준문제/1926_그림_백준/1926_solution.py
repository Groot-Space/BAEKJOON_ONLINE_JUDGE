from sys import stdin as f

def bfs(y, x, visited, mp, nm):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]

    queue = [[y,x]]
    visited[y][x] = 1
    count = 1
    while len(queue) != 0:
        point = queue.pop(0)
        for j in range(len(dirs)):
            _y = point[0] + dirs[j][0]
            _x = point[1] + dirs[j][1]
            if _y >= 0 and _x >= 0 and _y < nm[0] and _x < nm[1] and mp[_y][_x] == '1' and visited[_y][_x] == 0:
                queue.append([_y, _x])
                visited[_y][_x] = 1
                count += 1
    return count, visited


f = open("testcase.txt", 'r')
nm = list(map(int, f.readline().split())) #y,x
mp = []

for i in range(nm[0]):
    temp = f.readline().split()
    mp.append(temp)
visited = [[0 for i in range(nm[1])] for j in range(nm[0])]

count = 0
area = 0

for i in range(len(mp)):
    for j in range(len(mp[i])):
        if visited[i][j] == 0 and mp[i][j] == '1':
            c, visited = bfs(i, j, visited, mp, nm)
            count += 1
            if area < c:
                area = c

print(count)
if count == 0:
    print(0)
else:
    print(area)