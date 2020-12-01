
# 123 ~ 987 까지 후보군을 만드는 함수
# 각 후보에 대해 baseball의 값과 비교를 하여 같은 결과값이 나오는지 확인
# 1개의 guess, 1개의 후보에 대해 서로 일치하는지 확인하는 함수
# permutations에서 나오는 출력형태가 튜플인데 이를 문자로 전환해주는 함수
from itertools import permutations

LENGTH = 3

def solution(baseball):
    candidates = get_candidates(LENGTH)
    answer_count = 0
    for candidate in candidates:
        is_passed = check_candidate(baseball, candidate)
        if is_passed:
            answer_count += 1
    return answer_count

def get_candidates(length): #던질 수 있는 모든 경우의 수
    numbers = list(range(1, 10))
    candidates = list(permutations(numbers, length))
    return candidates

def check_candidate(baseball, candidate): #결과가 맞아 떨어지는지 확인
    is_passed = True
    for guess in baseball:
        correct = check(guess, candidate)
        if not correct:
            is_passed = False
            break
    return is_passed

def check(guess, candidate):
    guess_num, guess_strike, guess_ball = guess
    guess_num_str = str(guess_num)
    candidate_str = tuple_to_str(candidate)
    strike = 0
    ball = 0
    for str1, str2 in zip(guess_num_str, candidate_str):
        if str1 == str2:
            strike += 1
        elif str1 in candidate_str:
            ball += 1

    is_correct = True
    if strike != guess_strike or ball != guess_ball:
        is_correct = False
    return is_correct

def tuple_to_str(tuple_):
    result = ""
    for number in tuple_:
        result += str(number)
    return result

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))