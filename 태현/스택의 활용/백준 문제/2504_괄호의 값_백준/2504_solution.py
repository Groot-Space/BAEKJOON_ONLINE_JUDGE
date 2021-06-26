from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

check = deque()
arr = f.readline()
ans = deque()
ret = deque()
flag = 0
for i in range(len(arr)):
    if arr[i] == '(':
        ans.append('(')
        check.append('(')

    elif arr[i] == '[':
        ans.append('[')
        check.append('[')

    elif arr[i] == ')':
        if len(check) == 0 or check.pop() != '(':
            print(0)
            flag = 1
            break

        if len(ans) > 0 and arr[i-1] == '(':
            ans.pop()
            ans.append('2')

        else :
            ans.append(')')

    elif arr[i] == ']':
        if len(check) == 0 or check.pop() != '[':
            print(0)
            flag = 1
            break

        if len(ans) > 0 and arr[i-1] == '[':
            ans.pop()
            ans.append('3')
        else :
            ans.append(']')

if flag == 0:
    if len(check) != 0:
        print(0)
    else:
        i = 0
        while 1:
            if i >= len(ans):
                break

            if ans[i] == ')':
                tmp1 = 0
                while 1:
                    tmp2 = ret.pop()
                    if tmp2 == '(':
                        break
                    else:
                        tmp1 += int(tmp2)
                ret.append(tmp1 * 2)

            elif ans[i] == ']':
                tmp1 = 0
                while 1:
                    tmp2 = ret.pop()
                    if tmp2 == '[':
                        break
                    else:
                        tmp1 += int(tmp2)
                ret.append(tmp1*3)

            else:
                ret.append(ans[i])
            i += 1

        total = sum(map(int,ret))
        print(total)