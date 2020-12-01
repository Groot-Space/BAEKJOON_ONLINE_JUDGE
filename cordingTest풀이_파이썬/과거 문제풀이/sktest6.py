#1번 12345
#2번 21232425
#3번 3311224455
def solution(answers):
    answer = []

    lens = len(answers)
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    countdic = {'A': {'_C': 0, 'l' : 1}, 'B':{'_C': 0, 'l': 2},'C': {'_C': 0, 'l': 3}}
    countdic['A']['_C'] = counting(first, answers, lens)
    countdic['B']['_C'] = counting(second, answers, lens)
    countdic['C']['_C'] = counting(third, answers, lens)
    countdic = sorted(countdic, key = lambda k : countdic['k']['l'], reverse = True)
    print(countdic)


def counting(arr, answers, lens):
    time = lens // len(arr)
    time_d = lens % len(arr)
    if time != 0 : arr *= time
    count = 0
    for i in range(time_d):
        arr.append(arr[i])
    for j in range(len(answers)):
        if arr[j] == answers[j]:
            count += 1
    return count


    return answer
solution([1,2,3,4,5])