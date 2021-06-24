from copy import deepcopy

def permutation(arr,ret,k,tmp,isused):
    if len(tmp) == k:
        ret.append(deepcopy(tmp))
    else:
        for i in range(len(arr)):
            if isused[i] == False:
                tmp.append(arr[i])
                isused[i] = True
                permutation(arr,ret,k,tmp,isused)
                isused[i] = False
                tmp.pop()

def mul_permutation(arr,ret,k,tmp):
    if len(tmp) == k:
        ret.append(deepcopy(tmp))
    else:
        for i in range(len(arr)):
            tmp.append(arr[i])
            mul_permutation(arr,ret,k,tmp)
            tmp.pop()

def combination(arr,ret,k,tmp,l = 0):
    if len(tmp) == k:
        ret.append(deepcopy(tmp))
    else:
        for i in range(l,len(arr)):
            tmp.append(arr[i])
            combination(arr,ret,k,tmp,i+1)
            tmp.pop()



arr = ['a','b','c','d']
ret = []
tmp = []
k = 3
isused = [False,False,False,False]

# permutation(arr,ret,k,tmp,isused)
# mul_permutation(arr,ret,k,tmp)
combination(arr,ret,k,tmp,0)
print(ret)