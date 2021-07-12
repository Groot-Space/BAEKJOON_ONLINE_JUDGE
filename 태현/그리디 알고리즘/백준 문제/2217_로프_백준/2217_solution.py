from sys import stdin as f
f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])

rope = [int(f.readline().split()[0]) for i in range(n)]

rope = sorted(rope)

ans = 0

for i in range(len(rope)):
    tmp = rope[i] * n
    if ans < tmp:
        ans = tmp
    n -= 1
print(ans)