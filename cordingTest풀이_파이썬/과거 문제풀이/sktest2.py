def solution(participant, completion):
    # 마라톤 대회
    # 1명 빼고 모두 완주

    # 선수이름배열(participant), 완주 선수 이름(completion)이 담긴 배열이 주어짐
    # 완주못한 선수 이름 알아내기
    # 동명이인 가능성
    # 솔루션 - 필요기능 나열- !< 필요한 객체> *<필요한 메소드>
    # 선수이름배열에서 선수 이름을 순서대로* 픽! 및 동명이인 확인*, 있으면 카운트!
    # 픽된 이름을 완주자 명단에서 탐색*
    # 탐색시 다수 탐색되면 카운트!*.
    # 카운트 된 숫자와 사전에 카운트 한 숫자가 다르면* 그사람이 낙오자!
    # 탐색이 되지 않아도 그사람이 낙오자!
    countB = quick_sort(participant)
    countA = quick_sort(completion)
    answer = ''
    for i in range(0, len(countB) - 1):
        if countB[i] != countA[i]:
            answer = countB[i]
            return answer
        elif i == len(countB)-2:
            answer = countB[-1]
            return answer


def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))