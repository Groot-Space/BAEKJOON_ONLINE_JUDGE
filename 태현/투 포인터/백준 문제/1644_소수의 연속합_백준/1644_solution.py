from sys import stdin as f
from collections import deque

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
# n = 41
primes = deque([False for i in range(n+1)])
c_prime = deque()

for i in range(2,n+1):
    if primes[i] == True :
        continue
    else :
        primes[i] = True
        c_prime.append(i)
        j = 2
        while i*j < n:
            primes[i*j] = True
            j += 1

end = 0
total = 0
ans = 0
cur_total = 0

for start in range(len(c_prime)):
    while cur_total < n and end < len(c_prime):
        cur_total += c_prime[end]
        end += 1

    if cur_total == n:
        ans += 1

    cur_total -= c_prime[start]


print(ans)

