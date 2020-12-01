# 1번 12345
# 2번 21232425
# 3번 3311224455
def solution(answers):
    answer = []
    lens = len(answers)
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    countdic = {'A': {'_C': 0, 'l': 1}, 'B': {'_C': 0, 'l': 2}, 'C': {'_C': 0, 'l': 3}}
    print(countdic['A']['_C'])
    countdic['A']['_C'] = counting(answers, first, lens)
    countdic['B']['_C'] = counting(answers, second, lens)
    countdic['C']['_C'] = counting(answers, third, lens)

    countdic = list(countdic.values())

    countdic = sorted(countdic, key=lambda k: k['_C'], reverse=True)

    _temp = []
    for i in range(0, 3):
        if countdic[i]['_C'] >= 1:
            answer.append(countdic[i]['l'])
            _temp.append(countdic[i]['_C'])
    _counting = 1
    for i in range(1, len(_temp)):
        if _temp[i - 1] == _temp[i]:
            _counting += 1
    if _counting == len(_temp):
        answer = sorted(answer)
        return answer
    else:
        return answer


def counting(answers, arr, lens):
    count = 0
    times = lens // len(arr) if lens // len(arr) > 0 else 1
    t = arr * times
    j = 0
    for i in range(lens):
        if answers[i] == t[i]:
            count += 1
        elif i >= len(t):
            if answers[i] == t[j]:
                count += 1
            j += 1
    return count