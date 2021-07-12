from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
arr = list(map(int, f.readline().split()))
arr.sort()
def get_dist(start, end):
    return (0 - (start + end)) ** 2
def two_point_ver2(arr):
    end = len(arr) - 1
    cur = float('inf')
    _start = 0
    _end = 0
    start = 0
    while start < end:
        while arr[start] + arr[end] > 0:
            if get_dist(arr[start],arr[end]) < cur:
                _start = start
                _end = end
                cur = get_dist(arr[start], arr[end])
            if end - 1 > start:
                end -= 1
            else :
                break

        if get_dist(arr[start], arr[end]) < cur:
            _start = start
            _end = end
            cur = get_dist(arr[start], arr[end])
        start += 1

    return _start, _end

s,e = two_point_ver2(arr)

if arr[s] > arr[e] :
    print(arr[e], arr[s])
else :
    print(arr[s], arr[e])