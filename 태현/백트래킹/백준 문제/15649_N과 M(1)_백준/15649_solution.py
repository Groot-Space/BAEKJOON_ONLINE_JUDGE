f = open('testcase.txt', 'r')
n, m = list(map(int,f.readline().split()))


isused = [0 for i in range(n+1)]
def permutation(n, m, ret, isused):
    # print(ret)
    if len(ret) == m:
        for item in ret:
            print(item, end = ' ')
        print()
    else :
        for i in range(n):
            if isused[i+1] == 0:
                isused[i+1] = 1
                ret.append(i + 1)
                permutation(n, m, ret, isused)
                ret.pop()
                isused[i+1] = 0

ret = []
permutation(n, m, ret, isused)