from sys import stdin as f

f = open('testcase.txt','r')

n, m = list(map(int,f.readline().split()))
arr = list(map(int,f.readline().split()))

def two_pointer(arr,target):
    end = 0 # 포스팅에선 1로 맞추고 시작했지만, 코드 상 편의를 위해 0으로 맞추겠습니다.
    total = 0
    count = 0
    for start in range(len(arr)): # start 이동
        while total < target and end < len(arr): # end 이동
            total += arr[end]
            end += 1

        if total == target:
            count += 1
        total -= arr[start]

    return count


print(two_pointer(arr,m))