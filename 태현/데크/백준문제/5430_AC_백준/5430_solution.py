
f = open('testcase.txt', 'r')
tastcase = int(f.readline())


class dq:
    def __init__(self, l):
        self.q = l
        self.front = 0
        self.end = len(self.q)
        self.size = len(self.q)
        self.r = 1

    def set_r(self):
        self.r = self.r % 2

    def pop(self):
        if self.size == 0:
            return -1

        if self.r == 1:
            self.size -= 1
            temp = self.front
            self.front += 1
            return self.q[temp]
        else:
            self.size -= 1
            temp = self.end - 1
            self.end -= 1
            return self.q[temp]

    def print_dq(self):

        # if self.size == 0:
        #     return 'error'

        if self.r == 1:
            _ans = self.q[self.front:self.end]
            ans = '[' + ','.join(_ans) +']'
            return ans
        else:
            _ans = self.q[self.front:self.end]
            _ans.reverse()
            ans = '[' + ','.join(_ans) +']'
            return ans


for i in range(tastcase):
    oper = (f.readline()[:-1])
    N = int(f.readline())
    _temp = f.readline()[1:-2].split(',')
    # if N == 0:
    #     print('error')
    #     continue

    arr = dq(_temp)
    flag = 0

    for j in range(len(oper)):
        if oper[j] == 'R':
            arr.r += 1
            arr.set_r()

        else:
            if N == 0:
                print('error')
                flag = 1
                break
            ans = arr.pop()
            if ans == -1:
                flag = 1
                print('error')
                break
    if flag != 1:
        print(arr.print_dq())

'''

import sys
tastcase = int(sys.stdin.readline())


class dq:
    def __init__(self, l):
        self.q = l
        self.front = 0
        self.end = len(self.q)
        self.size = len(self.q)
        self.r = 1

    def set_r(self):
        self.r = self.r % 2

    def pop(self):
        if self.size == 0:
            return -1

        if self.r == 1:
            self.size -= 1
            temp = self.front
            self.front += 1
            return self.q[temp]
        else:
            self.size -= 1
            temp = self.end - 1
            self.end -= 1
            return self.q[temp]

    def print_dq(self):

        # if self.size == 0:
        #     return 'error'

        if self.r == 1:
            _ans = self.q[self.front:self.end]
            ans = '[' + ','.join(_ans) +']'
            return ans
        else:
            _ans = self.q[self.front:self.end]
            _ans.reverse()
            ans = '[' + ','.join(_ans) +']'
            return ans


for i in range(tastcase):
    oper = (sys.stdin.readline()[:-1])
    N = int(sys.stdin.readline())
    _temp = sys.stdin.readline()[1:-2].split(',')

    arr = dq(_temp)
    flag = 0

    for j in range(len(oper)):
        if oper[j] == 'R':
            arr.r += 1
            arr.set_r()

        else:
            if N == 0:
                print('error')
                flag = 1
                break
            ans = arr.pop()
            if ans == -1:
                flag = 1
                print('error')
                break
    if flag != 1:
        print(arr.print_dq())

'''