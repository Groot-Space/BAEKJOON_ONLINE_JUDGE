# def multiplication(a,b,c):
#     if b == 1:
#         return a % c
#     val = multiplication(a, b//2, c)
#     if (b % 2) == 0:
#         return (val * val) % c
#     elif (b % 2) == 1:
#         return (val * a) % c
def multiplication(a, n, b,c, d): #d는 직전 재귀의 계산값이 됩니다. 재귀함수 도입부에서는 d = a로 시작합니다.
    if n == b:
        print((d * a) % c)
    else:
        multiplication(a,n+1,b ,c, (d * a)%c)

f = open('testcase.txt', 'r')
a, b, c = list(map(int,f.readline().split()))
print(multiplication(a,1,b,c,a))
# print(multiplication(a,b,c))
