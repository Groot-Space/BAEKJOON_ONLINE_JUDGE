from sys import stdin as f
from collections import deque

n, d, k, c = list(map(int, f.readline().split()))
arr = [int(f.readline().split()[0]) for i in range(n)]

window = deque()
visited = [0 for i in range(d + 1)]

cur_max = 0
count = 0

for i in range(k):
    window.append(arr[i])
    visited[arr[i]] += 1
    if visited[arr[i]] == 1:
        count += 1

if visited[c] == 0:
    cur_max += count + 1
else:
    cur_max += count

i = 0
while i < len(arr):
    tmp = window.popleft()
    visited[tmp] -= 1

    if visited[tmp] == 0:
        count -= 1

    window.append(arr[(i + k) % n])
    visited[arr[(i + k) % n]] += 1
    if visited[arr[(i + k) % n]] == 1:
        count += 1

    if visited[c] == 0:
        cur_max = max(cur_max, count + 1)
    else:
        cur_max = max(cur_max, count)
    i += 1

print(cur_max)
