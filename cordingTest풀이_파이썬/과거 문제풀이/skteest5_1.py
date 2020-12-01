def solution(genres, plays):  # 노래장르 문자열 배열, 노래별 재생횟수 정수형 배열
    lens = len(genres)
    total = []
    genreset = []
    answer = []
    for i in range(lens):
        total.append([genres[i], i, plays[i]])

    for j in range(lens):
        if len(genreset) == 0:
            genreset.append([genres[j]])
        else:
            count = 0
            for k in range(len(genreset)):
                if count == 1:
                    break
                elif genreset[k][0] == genres[j]:
                    count += 1
            if count == 0:
                genreset.append([genres[j]])

    _t = total
    for k in range(len(genreset)):
        _count = 0
        m = 0
        l = len(_t)
        while l != 0 and m < l:
            if genreset[k][0] == _t[m][0]:
                _count += _t[m][2]
                _temp = _t[:m]
                _temp += _t[m+1:]
                _t = _temp
                l = len(_t)
            else :
                m += 1
        genreset[k].append(_count)
    genreset = quicsort(genreset)
    for n in genreset:
        _temp = []
        for o in range(lens):
            if n[0] == total[o][0]:
                _temp.append([total[o][1], total[o][2]])
        _temp = quicsort(_temp)
        for p in range(0, 2):
            answer.append(_temp[p][0])
    return answer


def quicsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][1]
    down, equal, up = [], [], []
    for num in arr:
        if num[1] > pivot:
            up.append(num)
        elif num[1] == pivot:
            equal.append(num)
        else:
            down.append(num)
    return quicsort(up) + equal + quicsort(down)


def quicsort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][2]
    down, equal, up = [], [], []
    for num in arr:
        if num[2] > pivot:
            up.append(num)
        elif num[2] == pivot:
            equal.append(num)
        else:
            down.append(num)
    return quicsort(up) + equal + quicsort(down)

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))