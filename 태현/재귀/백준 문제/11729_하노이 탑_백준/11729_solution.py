
def Hanoi(a, b, n):
    if n == 1:
        print(str(a) + ' ' + str(b))

    else:
        Hanoi(a, 6-a-b, n-1)
        print(str(a) + ' ' + str(b))
        Hanoi(6-a-b, b, n-1)

n = int(input())
print(2**n - 1)
Hanoi(1,3,n)
