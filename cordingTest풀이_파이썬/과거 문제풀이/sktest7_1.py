def solution(answers):
    peoplePatternArray = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scoreArray = [0,0,0]
    result = []

    for idx, answer in enumerate(answers):
        for i in range(0,len(peoplePatternArray)):
            if answer == peoplePatternArray[i][idx%len(peoplePatternArray[i])]:
                scoreArray[i] += 1

    for idx, s in enumerate(scoreArray):
        if s == max(scoreArray):
            result.append(idx+1)
    return result
solution([1,2,3,4,5])