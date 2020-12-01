def solution(numbers):
    _list = []
    purmutation(numbers, '', _list)
    _list = list(set(_list))
    for i, value in enumerate(_list):
        if value[0] == '0':
            _list[i] = value[1:]
    _list = list(set(_list))
    for j in range(0, len(_list) - 1):
        if _list[j] == '':
            _list = _list[:j] + _list[j + 1:]
    _list = list(map(int, _list))
    sorted(_list, reverse=True)
    answer = 0
    for k , v in enumerate(_list):
        if isPrimeNumber(v) == True:
                answer += 1

    return answer
def isPrimeNumber(number):
    if number <= 1:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True


def purmutation(arr, prefix, _list):
    if len(arr) == 0:
        if prefix != None:
            _list.append(prefix)
            return _list
    else:
        for i in range(0, len(arr)):
            _arr = arr[0:i] + arr[i + 1:]
            _prefix = prefix + arr[i]
            if len(_arr) >= 1:
                purmutation(_arr, '', _list)
            purmutation(_arr, _prefix, _list)


print(solution("011"))