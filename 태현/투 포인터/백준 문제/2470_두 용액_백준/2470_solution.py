from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
arr = list(map(int, f.readline().split()))

def get_dist(start, end):
    tmp = abs(0 - (start + end))
    return tmp

def two_pointer(arr):
    _start = 0
    _end = 0
    end = 1
    cur = float('inf')
    for start in range(len(arr)):
        while end < len(arr) and arr[start] + arr[end] > 0:
            if get_dist(start)
            _start = start
            _end = end
            cur = get_dist(arr[start], arr[end])
            end += 1

    return _start, _end

s, e = two_pointer(arr)
if arr[s] > arr[e] :
    print(arr[e], arr[s])
else :
    print(arr[s], arr[e])