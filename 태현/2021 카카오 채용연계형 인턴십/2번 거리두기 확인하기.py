from collections import deque


def check2(place, _i, y, x):
    # 상 하 좌 우
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))  # 하, 상, 우, 좌
    for i in range(len(dirs)):
        if i != _i:
            new_y = y + dirs[i][0]
            new_x = x + dirs[i][1]
            if new_y >= 0 and new_y < len(place) and new_x >= 0 and new_x < len(place[0]):
                if place[new_y][new_x] == 'P':
                    return 0
    return 1


def check1(place, queue, dirs):
    while len(queue) > 0:
        cur = queue.popleft()
        for i in range(len(dirs)):
            new_y = cur[0] + dirs[i][0]
            new_x = cur[1] + dirs[i][1]

            if new_y >= 0 and new_y < len(place) and new_x >= 0 and new_x < len(place[0]):
                if place[new_y][new_x] == 'P':
                    return 0
                elif place[new_y][new_x] == 'O':
                    if check2(place, i, new_y, new_x) == 0:
                        return 0
    return 1


def solution(places):
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    ans = []
    for place in places:
        queue = deque()

        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    queue.append((i, j))
        ans.append(check1(place, queue, dirs))
    return ans