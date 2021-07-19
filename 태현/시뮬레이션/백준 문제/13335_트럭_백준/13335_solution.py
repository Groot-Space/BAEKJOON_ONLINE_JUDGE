from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')
n, w, l = list(map(int, f.readline().split()))
truck = deque(list(map(int,f.readline().split())))
bridge = deque([0 for i in range(w)])
bridge_weight = 0
t = 0

while len(truck) > 0:
    while len(truck) > 0  and bridge_weight + truck[0] <= l:
        t += 1
        bridge.appendleft(truck.popleft())
        bridge_weight -= bridge.pop()
        bridge_weight += bridge[0]

    while len(truck) > 0  and bridge_weight + truck[0] > l:
        t += 1
        bridge_weight -= bridge.pop()
        if bridge_weight + truck[0] <= l:
            bridge.appendleft(truck.popleft())
            bridge_weight += bridge[0]
        else:
            bridge.appendleft(0)



print(t + len(bridge))
