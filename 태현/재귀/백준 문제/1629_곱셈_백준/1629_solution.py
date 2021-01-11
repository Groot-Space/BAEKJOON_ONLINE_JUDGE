def multiplication(a,b,c):
    if b == 1:
        return a % c
    val = multiplication(a, b//2, c)
    if (b % 2) == 0:
        return (val * val) % c
    elif (b % 2) == 1:
        return (val * a) % c

f = open('testcase.txt', 'r')
a, b, c = list(map(int,f.readline().split()))
print(multiplication(a,b,c))
