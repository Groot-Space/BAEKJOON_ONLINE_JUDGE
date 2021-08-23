from sys import stdin as f

f = open('testcase.txt', 'r')

n = int(f.readline().split()[0])
arr = list(map(int, f.readline().split()))
arr.sort()
def get_dist(start, end):
    return (0 - (start + end)) ** 2

# def two_pointer_ver2(arr):
#     end = len(arr) - 1
#     start = 0
#     total = arr[0] + arr[len(arr)-1]
#     min_score = float('inf')
#     ret = [0,0]
#
#     while start < end-1:
#         while total > 0 and start < end-1 and get_dist(total) >= min_score:
#             total = arr[start] + arr[end]
#             end -= 1
#
#         while total < 0 and start < end-1 and get_dist(total) >= min_score:
#             total = arr[start] + arr[end]
#             start += 1
#
#         ret[0] = start
#         ret[1] = end
#         min_score = get_dist(total)
#
#     return ret
def two_point_ver2(arr):
    end = len(arr) - 1
    cur = float('inf')
    start = 0
    ret = [start, end]
    while start < end:

        while arr[start] + arr[end] > 0: #합이 0보다 크면 end를 왼쪽으로

            if get_dist(arr[start],arr[end]) < cur: #왼쪽으로 땡기는데, min값이 나오면 갱신
                ret[0] = start
                ret[1] = end
                cur = get_dist(arr[start], arr[end])

            if end - 1 > start: #start보다 클 때까지 end를 땡김
                end -= 1
            else :
                break

        if get_dist(arr[start], arr[end]) < cur: #합이 0보다 크지 않은데 합이 최소일 경우
            ret[0] = start
            ret[1] = end
            cur = get_dist(arr[start], arr[end])

        start += 1

    return ret

s,e = two_point_ver2(arr)

if arr[s] > arr[e] :
    print(arr[e], arr[s])
else :
    print(arr[s], arr[e])