f = open('testcase2.txt','r')

line_num = int(f.readline().rstrip())
stack = []
ret = 0
for i in range(line_num):
    num = int(f.readline().rstrip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for j in stack:
    ret += j

print(ret)


'''
import sys

line_num = int(sys.stdin.readline().rstrip())
stack = []
ret = 0
for i in range(line_num):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

for j in stack:
    ret += j

print(ret)



'''