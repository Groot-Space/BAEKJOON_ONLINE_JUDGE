from sys import stdin as f
# f = open('testcase.txt', 'r')
line = f.readline().rstrip()
# print(line)
while True:
    flag = 0
    if len(line) == 1 and line[0] =='.':
        break

    stack = []
    for i in range(len(line)):
        if line[i] == '(' or line[i] == '[':
            stack.append(line[i])
            # print(stack)
        elif line[i] == ')' or line[i] == ']':
            if len(stack) == 0:
                print('no')
                flag += 1
                break

            temp = stack.pop()
            # print('확인 :', temp,line[i])
            if line[i] == ')':
                if temp != '(':
                    print('no')
                    flag += 1
                    break

            elif line[i] == ']':
                if temp != '[':
                    print('no')
                    flag += 1
                    break


    if flag != 1:
        if len(stack) == 0:
            print('yes')
        else :
            print('no')

    line = f.readline().rstrip()
    # print(line)