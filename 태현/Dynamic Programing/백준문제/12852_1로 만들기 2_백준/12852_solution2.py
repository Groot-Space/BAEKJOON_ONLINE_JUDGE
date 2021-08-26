from sys import stdin as f

n = int(f.readline().split()[0])
arr = [0 for i in range(10**6 +1)]
arr[1] = 0
arr[2] = 1
arr[3] = 1

ret = [0,1,1,1]

def ret_print(ret,idx):
    if ret[idx] != 1:
        print(ret[idx], end = ' ')
        ret_print(ret, ret[idx])
    else :
        print(1)
def dynamic2(arr, n,ret):
    for i in range(4, n+1):
        arr[i] = arr[i-1] + 1
        _ret = i - 1
        if i % 3 == 0:
            tmp = arr[i//3] + 1
            if tmp < arr[i]:
                arr[i] = tmp
                _ret = i // 3
        if i % 2 == 0:
            tmp = arr[i//2] + 1
            if tmp < arr[i]:
                arr[i] = tmp
                _ret = i // 2
        ret.append(_ret)
    ret.append(n)

    print(arr[n])
    ret_print(ret, len(ret)-1)
dynamic2(arr,n,ret)


