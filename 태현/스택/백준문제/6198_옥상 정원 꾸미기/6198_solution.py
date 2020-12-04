f = open('testcase.txt', 'r')
building_count = int(f.readline())
building = [int(f.readline()) for i in range(building_count)]
stack = []
total = 0
for j in range(len(building)):
    while len(stack) != 0 and stack[len(stack)-1] <= building[j]:
        stack.pop()
    total += len(stack)
    stack.append(building[j])
print(total)


'''
import sys
building_count = int(sys.stdin.readline())
building = [int(sys.stdin.readline()) for i in range(building_count)]
stack = []
total = 0
for j in range(len(building)):
    while len(stack) != 0 and stack[len(stack)-1] <= building[j]:
        stack.pop()
    total += len(stack)
    stack.append(building[j])
print(total)
'''