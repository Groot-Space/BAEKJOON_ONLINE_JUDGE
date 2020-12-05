import sys
N = int(sys.stdin.readline())
q = [i for i in range(1,N+1)]
front = 0
end = N - 1
count = 1
length = N

while length > 1 :
    if (count % 2) != 0:
        front += 1
        length -= 1
        count += 1
    else :
        q.append(q[front])
        front += 1
        count += 1
print(q[front])