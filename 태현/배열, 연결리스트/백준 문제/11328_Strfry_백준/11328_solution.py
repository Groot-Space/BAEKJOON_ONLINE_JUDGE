'''
f = open('strfry_테스트케이스.txt','r')
testcase = int(f.readline())

def solve(text):
    j = 0
    alpha = [0] * 26
    for i in range(len(text[0])):
        idx1 = ord(text[0][i]) % 26
        alpha[idx1] += 1
        idx2 = ord(text[1][i]) % 26
        alpha[idx2] -= 1

    for j in alpha:
        if j != 0:
            return 'Impossible'
    return 'Possible'

for i in range(testcase):
    text = f.readline().split()
    print(solve(text))
'''

import sys
testcase = int(sys.stdin.readline())

def solve(text):

    if len(text[0]) != len(text[1]):
        return 'Impossible'

    j = 0
    alpha = [0] * 26

    for i in range(len(text[0])):
        idx1 = ord(text[0][i]) % 26
        alpha[idx1] += 1
        idx2 = ord(text[1][i]) % 26
        alpha[idx2] -= 1

    for j in alpha:
        if j != 0:
            return 'Impossible'
    return 'Possible'

for i in range(testcase):
    text = sys.stdin.readline().split()
    print(solve(text))
