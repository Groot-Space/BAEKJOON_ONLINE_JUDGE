# 장르별 가장 많이 재생된 노래 두개씩 선택 - 장르 여러개 , 노래 두개씩
# 노래는 고유번호로 구분
# 수록기준 - 노래가 가장 많이 재생된 장르, 장르 내에 많이 재생된 노래 먼저 수록, 재생횟수가 같을 경우 고유번호 낮은 순서로 수록
# 장르숫자가 제일 많은 것 -> 장르 내에 재생 수가 많은 순 -> 그다음 장르 ->장르 내 재생 수
# 장르를 키로, plays를 값으로 저장

def solution(genres, plays):  # 노래장르 문자열 배열, 노래별 재생횟수 정수형 배열
    hashlen = len(genres)
    hashtable = hashmake(genres, hashlen)
    hashtable = hashtableappend(hashtable, genres, hashlen, plays)
    answer = []
    hashtable = quicsort(hashtable)
    _getindex = []
    for i in range(len(hashtable)):
        _temp = []
        if hashtable[i][0] != '':
            for j in range(len(genres)):
                if genres[j] == hashtable[i][0]:
                    _temp.append([j, plays[j]])
            _temp = quicsort(_temp)
            for l in range(0,2):
                _getindex.append(_temp[l][0])
    return _getindex


def hashtableappend(hashtable, genres, arr_len, plays):
    for i in range(len(genres)):
        index = hashfunction(genres[i], arr_len)
        if hashtable[index] == ['', 0]:
            hashtable[index] = [genres[i], plays[i]]
        elif hashtable[index][0] == genres[i]:
            hashtable[index][1] += plays[i]
        else:
            for j in range(i, len(genres[i])):
                index += 1
                if index <= len(hashtable) - 1 and hashtable[index] == ['', 0]:
                    hashtable[index].append([genres[i], plays[i]])
                else:
                    for k in range(0, i):
                        index = k
                        if index <= len(hashtable) - 1 and hashtable[index] == ['', 0]:
                            hashtable[index].append([genres[i], plays[i]])

    return hashtable


def hashmake(genres, hashlen):  # 필요 크기만큼 2중배열을 만들어주는 역할.
    hashtable = []
    for i in range(hashlen):
        hashtable.append(['', 0])
    return hashtable


def hashfunction(key, arr_len):  # 문자열, 배열길이
    _hashresult = []
    result = 0
    for i in range(len(key)):
        _hashresult.append(ord(key[i]))
    for j in range(len(_hashresult)):
        result += _hashresult[j]
    result %= arr_len
    return result


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

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))