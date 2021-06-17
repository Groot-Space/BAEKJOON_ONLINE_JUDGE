from sys import stdin as f
f = open('testcase.txt', 'r')

_ = f.readline()
arr1 = list(map(int,f.readline().split()))
_ = f.readline()
arr2 = list(map(int,f.readline().split()))

arr1.sort()

def biserch(arr,st,en,mid,target):
    while st <= en:
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            en = mid - 1
            mid = (st + en) // 2
        elif arr[mid] < target:
            st = mid + 1
            mid = (st + en) // 2
    return 0

st = 0
en = len(arr1)-1
mid = (st + en) // 2
for i in arr2:
    print(biserch(arr1,st,en,mid,i))