'''
f = open('testcase.txt', 'r')

tastcase = int(f.readline())

class Queue:
    def __init__(self):
        self.max = 2000000
        self.front = 0
        self.end = 0
        self.q = []
        self.length = 0

    def empty(self,):
        if self.length == 2000000 :
            return 0 #안비어 있음
        else:
            return 1

    def _empty(self):
        if self.length == 0:
            return 1
        else:
            return 0

    def push(self, item):
        if self.empty() == 1:
            self.q.append(item)
            self.end = (self.end + 1) % self.max
            self.length += 1

    def back(self):
        if self.length >= 1:
            if self.end == 0:
                return self.q[len(self.q)]
            else:
                return self.q[(self.end-1)]
        else:
            return -1

    def size(self):
        return self.length

    def pop(self):
        if self.length >= 1:
            _temp = self.front
            self.front = (self.front + 1) % self.max
            self.length -= 1
            return self.q[_temp]
        else :
            return -1

    def _front(self):
        if self.length >= 1:
            return self.q[self.front]
        else:
            return -1

q = Queue()
for i in range(tastcase):
    oper = f.readline().split()
    if oper[0] == 'push':
        q.push(int(oper[1]))
    elif oper[0] == 'front':
        print(q._front())
    elif oper[0] == 'back':
        print(q.back())
    elif oper[0] == 'empty':
        print(q._empty())
    elif oper[0] == 'pop':
        print(q.pop())
    elif oper[0] == 'size':
        print(q.size())
'''
import sys

tastcase = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.max = 2000000
        self.front = 0
        self.end = 0
        self.q = []
        self.length = 0

    def empty(self,):
        if self.length == 2000000 :
            return 0 #안비어 있음
        else:
            return 1

    def _empty(self):
        if self.length == 0:
            return 1
        else:
            return 0

    def push(self, item):
        if self.empty() == 1:
            self.q.append(item)
            self.end = (self.end + 1) % self.max
            self.length += 1

    def back(self):
        if self.length >= 1:
            if self.end == 0:
                return self.q[len(self.q)]
            else:
                return self.q[(self.end-1)]
        else:
            return -1

    def size(self):
        return self.length

    def pop(self):
        if self.length >= 1:
            _temp = self.front
            self.front = (self.front + 1) % self.max
            self.length -= 1
            return self.q[_temp]
        else :
            return -1

    def _front(self):
        if self.length >= 1:
            return self.q[self.front]
        else:
            return -1

q = Queue()
for i in range(tastcase):
    oper = sys.stdin.readline().split()
    if oper[0] == 'push':
        q.push(int(oper[1]))
    elif oper[0] == 'front':
        print(q._front())
    elif oper[0] == 'back':
        print(q.back())
    elif oper[0] == 'empty':
        print(q._empty())
    elif oper[0] == 'pop':
        print(q.pop())
    elif oper[0] == 'size':
        print(q.size())
