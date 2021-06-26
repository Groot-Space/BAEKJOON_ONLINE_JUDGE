from sys import stdin as f

f = open('testcase.txt', 'r')

stack = f.readline()
# "(((()))))"

total = 0 #막대 갯수
bar = 0
new_bar = 0
for i in range(len(stack)):
    if stack[i] == "(":
        bar += 1
        new_bar += 1
    elif stack[i] == ")":
        if i != 0 and stack[i-1] == "(": #레이져일때
            bar -= 1
            new_bar -= 1
            if total == 0:
                total += bar * 2
                new_bar = 0
            else :
                total += bar + new_bar
                new_bar = 0
        else :
            bar -= 1

print(total)