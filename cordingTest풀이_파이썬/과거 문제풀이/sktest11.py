#프로그래머스 카펫 문제
# 1. 전체 카펫 수를 구함. 24 + 24 = 48
# 2. 1번에서 구한 값의 약수를 구함. 48의 약수는 2,3, 4, 12, 16
# 3. 가로와 세로의 길이를 약수, 전체 카펫수 // 약수를 통해 정함
# 4. 조건에 맞으면 가로길이가 세로길이보다 크거나 같게 바꿔줌.
def solution(brown, red):
    total = brown + red
    factors = get_factors(total)
    width, height = 0, 0
    for factor in factors:
        width, height = factor, total // factor #면적을 구성하는 약수들
        size = width*height # 면적 구하기.
        boarder = 2*width + 2*(height-2) #회색 부분 구하기 테두리
        if size - boarder == red:
            break
    if width < height:
        width, height = height, width
    answer = [width, height]
    return answer

#약수 구하기
    #1. 타겟을 제곱근 함.
    #2. 1부터 제곱근한 값 중에서 나눠 떨어지는 값을 찾음.
    #3. 나눠 떨어지는 값을 찾으면 결과 배열에 추가함.
    #4. 몫도 결과값에 추가함.
    #5. 그걸 리턴.
def get_factors(target):
    result = set([])
    root_of_target = int(target**0.5)
    for candidate in range(1, root_of_target + 1):
        if target % candidate == 0:
            result.add(candidate) #집합에 추가할 때에는 add를 사용.
            result.add(target//candidate)
    return result