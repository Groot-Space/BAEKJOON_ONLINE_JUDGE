import sys
first_line = sys.stdin.readline().split()
N = int(first_line[0])
target_num = int(first_line[1])
targets = list(map(int, sys.stdin.readline().split()))
haf = N//2
arr = [i for i in range(1, N+1)]
arr2 = arr.copy()
# print(stack)
# print(targets)
# print(N)
count = 0
#
def finding(arr, target):
    haf = len(arr) // 2
    haf += 1
    for i, t in enumerate(arr):
        if t == target:
            if (i+1) <= haf:
                return ('L', i)
            else:
                return ('R', i)

for i in range(target_num):
    target = targets[i]
    print("target " ,target)
    # moving = 0
    if arr[0] == target:
        arr = arr[1:]
        continue
    side, idx = finding(arr,target)
    print(arr)
    if side == 'L':
        temp = arr[:idx]
        arr = arr[idx+1:] + temp
        count += len(temp)
    else:
        temp = arr[idx+1:]
        arr = temp + arr[:idx]
        count += (len(temp)+1)
    print(side, idx)
    print(count)
print(arr)
print(count)