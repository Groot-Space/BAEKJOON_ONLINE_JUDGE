from collections import deque

def insert(linked_list, i, cur, used):
    linked_list[i][1] = i
    linked_list[cur][2] = i
    linked_list[i][0] = cur
    used += 1
    return i, used

def erase(linked_list, cur, used, erased):
    tmp = [cur, linked_list[cur][0]]
    before = linked_list[cur][0]
    after = linked_list[cur][2]
    used -= 1
    erased.append(tmp)
    if after != -1: #현재 위치가 맨 마지막이 아니라면,
        linked_list[before][2] = after
        linked_list[after][0] = before
        linked_list[cur][0] = -1
        linked_list[cur][2] = -1
        return after, used
    else :
        linked_list[before][2] = -1
        linked_list[cur][0] = -1
        # linked_list[cur][1] = -1
        return before, used

def recover(erased, linked_list, used):
    item, before = erased.pop()
    after = linked_list[before][2]
    used += 1
    if after != -1:
        linked_list[before][2] = item
        linked_list[after][0] = item
        linked_list[item][0] = before
        linked_list[item][2] = after
        return used
    else :
        linked_list[before][2] = item
        linked_list[item][0] = before
        return used

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

def solution(n, k, cmd):
    answer = ["X" for i in range(n+1)]
    linked_list = [[-1, -1, -1] for i in range(1000000)]
    cur = 0
    used = 0
    erased = deque()  # 지운 곳, 지우기 전 노드

    for i in range(1,n+1):
        cur, used = insert(linked_list, i, cur, used)

    cur = k+1
    for query in cmd:
        query_splited = query.split()
        if query_splited[0] == "U":
            for i in range(int(query_splited[1])):
                cur = linked_list[cur][0]
        elif query_splited[0] == "D":
            for i in range(int(query_splited[1])):
                cur = linked_list[cur][2]
        elif query_splited[0] == "C":
            cur, used = erase(linked_list, cur, used, erased)
        else :
            used = recover(erased, linked_list, used)

    _cur = linked_list[0][2]
    for i in range(used):
        # print(linked_list[_cur][1], end = ' ')
        answer[linked_list[_cur][1]] = 'O'
        _cur = linked_list[_cur][2]

    print(''.join(answer[1:]))
solution(n,k,cmd)

