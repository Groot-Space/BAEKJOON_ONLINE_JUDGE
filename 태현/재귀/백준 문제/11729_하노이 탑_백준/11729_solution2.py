
def Hanoi(a, b, n, out):
    if n == 1:
        out = [str(a) + ' ' + str(b)]
        return 1, out

    else:
        count, out = Hanoi(a, 6-a-b, n-1, out)
        out.append(str(a) + ' ' + str(b))
        count += 1
        _out = []
        _count, _out = Hanoi(6-a-b, b, n-1, _out)
        out += _out
        return count+_count, out

n = int(input())
# print(2**n - 1)
out = []
count, out = Hanoi(1,3,n, out)
print(count)
for i in out:
    print(i)