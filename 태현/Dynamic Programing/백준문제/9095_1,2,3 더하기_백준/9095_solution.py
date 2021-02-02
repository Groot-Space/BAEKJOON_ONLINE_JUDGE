from sys import stdin as f
# f = open('testcase.txt', 'r')
tastcase = list(map(int,f.readline().split()))
test_k = []

for i in range(tastcase[0]):
    test_k.append(list(map(int,f.readline().split()))[0])

d = [-1 for i in range(12)]

d[1] = 1
d[2] = 2
d[3] = 4
for i in test_k:
    for j in range(4,i+1):
        _temp = 0
        if j - 1 > 0:
            _temp += d[j-1]
        if j - 2 > 0:
            _temp += d[j-2]
        if j - 3 > 0:
            _temp += d[j-3]
        d[j] = _temp
    print(d[i])