def solution(priorities, location):
    locationlist = []
    answer = 0
    for i in range(0, len(priorities)):
        if i == location:
            locationlist.append(True)
        else:
            locationlist.append(False)
    while(True):
        _temp = priorities[0]
        flag = True #위치 바꿧는지 판별 true면 안바꿈
        for i in range(1, len(priorities)): #우선순위가 큰게 있는지 확인
            if _temp < priorities[i]: #출력대상보다 우선순위가 높은 것이 있는지 탐색
                flag = False #있으면 위치를 바꿈
                priorities = priorities[1:]
                priorities.append(_temp)
                location, locationlist = locationexchange(priorities, locationlist, location)
                break

            elif _temp == priorities[i] and locationlist[0] == False: #보다 높은 우선순위가 없고, 같은 것들 만 잇을 때 출력
                priorities = priorities[1:]
                locationlist.pop(0)
                answer += 1
                break

        if flag == True and locationlist[0] == False: #위치를 바꿀 필요가 없는 상태에서 알고싶은 대상이 아닐경우 출력
            priorities.pop(0)
            locationlist.pop()
            if len(priorities) == 0:
                return answer
            else :
                answer += 1

        elif (flag == True) and (locationlist[0] == True): #위치를 바꿀 필요가 없는 상태에서 알고 싶은 대상일 경우
            answer += 1
            return answer

def locationexchange(priorities, locationlist, location):
    if location > 0:
        locationlist[location] = False
        locationlist[location - 1] = True
        location -= 1
    else:
        locationlist[0] = False
        locationlist[-1] = True
        location = len(priorities) - 1
    return location, locationlist

print(solution(	[2, 1, 3, 2], 2))