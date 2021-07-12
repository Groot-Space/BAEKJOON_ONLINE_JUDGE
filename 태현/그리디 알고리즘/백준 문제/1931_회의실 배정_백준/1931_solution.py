from sys import stdin as f

f = open('testcase.txt', 'r')
n = int(f.readline().split()[0])
scedule = [[0,0] for i in range(n)]

for i in range(n):
    scedule[i][0], scedule[i][1] = list(map(int, f.readline().split()))

scedule = sorted(scedule, key = lambda x : (x[1],x[0]))
time_table = [False for i in range(24)]

count = 0
end = 0
for i in scedule:
    if end <= i[0]:
        count += 1
        end = i[1]
print(count)