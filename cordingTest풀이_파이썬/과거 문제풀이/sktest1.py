def solution(progresses, speeds):
# 100%일때 반영, 개발속도는 다르지만 배포는 함께,
# 개발속도의 큐와 배포순서가 적힌 큐가 주어짐,
# 각 배포때마다 몇개의 기능이 배포되는지 알아내야 함.
# 배포는 하루에 한번. 하루 끝에 이루어짐,
# 진도율 95퍼짜리는 2일 뒤에 이루어짐

# 남은 진도율을 구하는 기능
# 남은 진도율을 속도로 나누어서 몇일이 걸리는지 알아보는 기능, 리스트저장
# 일수별로 몇개의 작업이 끝나는지 묶는 기능
# 기준 day를 정함.
# 첫 번째 기준 day는 첫 번째 작업기준 2차원 배열 0,0에 저장.
# 만약 첫 기준 day보다 늦게 끝나는 작업이 생기면 그게 두번 째 기준이 됨. 1,0에 저장

    stdday = getprogresses(progresses[0], speeds[0])
    dayslist = []
    dayslist.append([stdday])
    dayslist[0].append(1)
    for i in range(1, len(progresses)):
        _temp = getprogresses(progresses[i], speeds[i])
        _idx = len(dayslist) - 1
        if _temp <= stdday:
            dayslist[_idx][1] = dayslist[_idx][1] + 1
        else :
            stdday = _temp
            dayslist.append([stdday,1])

    answer = []
    for i in range(0, len(dayslist)):
        answer.append(dayslist[i][1])
    return answer

def getprogresses(progress, speed):
    days = (100 - progress) // speed
    return days




solution([93,30,55],[1,30,5])