from collections import deque


def get_parent(parent, x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def check_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return 1
    else:
        return 0


def solution(n, v1, v2, num, amount):  # n = 학생 수, v1 v2 = 팀, num = 상점받은 학생, amount = 상점
    parent = [i for i in range(n + 1)]
    for i in range(len(v1)):
        union(parent, v1[i], v2[i])

    answer = dict()
    for i in range(len(num)):
        leader = get_parent(parent, num[i])
        if leader in answer:
            answer[leader] += amount[i]
        else:
            answer[leader] = amount[i]

    for i in range(len(v1)):
        tmp1 = get_parent(parent, v1[i])
        tmp2 = get_parent(parent, v2[i])
        if tmp1 != tmp2:
            if tmp1 not in answer:
                answer[tmp1] = 0
            if tmp2 not in answer:
                answer[tmp2] = 0
        elif tmp1 == tmp2:
            if tmp1 not in answer:
                answer[tmp1] = 0

    sdict = sorted(answer.items(), key=lambda x: x[1], reverse=True)

    top_list = deque()
    top_list.append(sdict[0][0])
    for i in range(1, len(sdict)):
        if sdict[i][1] == sdict[0][1]:
            top_list.append(sdict[i][0])
        else:
            break

    if len(top_list) == 1:
        return top_list[0]
    else:
        return sorted(top_list)[0]
n = 10
v1 = [1, 10, 6, 5, 6, 9]
v2 = [3, 7, 2, 8, 7, 3]
num = [3, 4, 5, 1, 8, 7, 9, 2]
amount = [10, 5, 6, -6, -8, 2, -2, 5]
solution(n, v1, v2, num, amount)