from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0]) # 컴퓨터 대수

k = int(f.readline().split()[0]) # 컴퓨터 연결 쌍

computers = [i for i in range(n+1)]
grouping = [0 for i in range(n+1)]

def get_parent(arr, idx):
    if arr[idx] == idx:
        return arr[idx]
    else :
        arr[idx] = get_parent(arr, arr[idx])
        return arr[idx]

def union(arr, a, b, grouping):
    parent_a = get_parent(arr, a)
    parent_b = get_parent(arr, b)
    if parent_a < parent_b:
        arr[parent_b] = parent_a
        grouping[parent_a] += 1 + grouping[parent_b]
    elif parent_b < parent_a :
        arr[parent_a] = parent_b
        grouping[parent_b] += 1 + grouping[parent_a]

for i in range(k):
    a, b = list(map(int, f.readline().split()))
    union(computers, a, b, grouping)

print(grouping[1])

