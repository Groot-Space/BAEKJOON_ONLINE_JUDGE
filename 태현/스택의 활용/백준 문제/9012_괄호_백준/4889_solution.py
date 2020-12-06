f = open('testcase.txt', 'r')
num = 1
while True:
    line = f.readline().rstrip()
    # print(line)
    if line[0] == '-':
        break
    stack = []
    change = 0

    for i in range(len(line)):

        if line[i] == '{' :
            stack.append(line[i])

        elif line[i] == '}':
            if len(stack) == 0:
                stack.append('{')
                change += 1
            else :
                stack.pop()

    change += (len(stack) // 2)
    print(str(num) + '. ' + str(change))
    num += 1
