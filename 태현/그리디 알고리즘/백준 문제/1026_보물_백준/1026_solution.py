from sys import stdin as f

f = open('testcase.txt','r')
n = int(f.readline().split()[0])
A = list(map(int, f.readline().split()))
B = list(map(int,f.readline().split()))

A.sort()
# print(A)
B.sort(reverse=True)
t = 0
for i in range(len(A)):
    t += A[i] * B[i]
print(t)
