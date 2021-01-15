test = [1,2,3,4]

def combination(test,ret,result):
    if len(ret) == len(test):
        result.append(ret)
    else:
        for i in test:
            combination(test, ret + [i],result)
        return result
ret = []
result = []
print(combination(test,ret,result))