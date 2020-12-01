# 서로 다른 옷의 조합 수 리턴
# [의상이름, 의상종류] 의상 수는 1개 이상 30개 이하
# 의상종류 headgear, eyewear
# 모든 원소 문자열
# 하루에 입는 의상은 최소 1개.

# 해법 : 모든 경우의 수 = 모자 갯수 * 상의 갯수 * 하의 갯수
# 모자를 안 썻을 경우 = 투명모자라고 놓음
# 모든 경우의 수 + 특정 의상 안썻을 경우 = 모자갯수 +1 * 상의 갯수+1 * 하의 갯수+1
# 단, +1을 해줌으로써 아무것도 안썻을 경우가 생겨버리므로, -1을 해줌.(반드시 1개는 장착)
def solution(clothes):  # [의상이름, 의상종류]
    totalclothescount = 0
    clothescategory = []
    answer = 0
    for i in clothes:
        totalclothescount += 1
        if len(clothescategory) >= 1:
            for k in range(0, len(clothescategory)):
                if clothescategory[k][1] == i[1]:
                    clothescategory[k].append(i[0])
                    break
                elif k == len(clothescategory) - 1:
                    clothescategory.append(i)
        else:
            clothescategory.append(i)
    _temp = 1
    for l in range(0, len(clothescategory)):
        _temp *= len(clothescategory[l])
    answer = _temp - 1

    return answer