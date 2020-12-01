def solution(genres, plays):  # 노래장르 문자열 배열, 노래별 재생횟수 정수형 배열
    d = {}
    for i in range(len(genres)):
        if not genres[i] in d:
            d[genres[i]] = {'t': 0, 'l': []}  # t = 전체 재생횟수, l = 노래정보
        # key = 장르이름, 값 = 전체 재생시간 , 노래정보리스트
        # 노래정보리스트는 2개 딕션너리로 구성.
        # 첫 번째는 key = v, value = 재생횟수
        # 두 번째는 key = i, value = 고유번호

        d[genres[i]]['l'].append({'v': plays[i], 'i': i})
        # 딕셔너리 각 장르의 노래정보리스트에 재생횟수와 고유번호를 추가.
        d[genres[i]]['t'] += plays[i]
    # 딕셔너리 각 장르의 총 시간에 재생시간을 더해줌.
    print(d)
    d = list(d.values())
    print(d)
    print(d[0]['t'])
    answer = []
    d = sorted(d, key=lambda k: k['t'], reverse=True)

    for i in range(len(d)):
        v = d[i]['l']
        v = sorted(v, key=lambda k: k['v'], reverse=True)
        for j in range(2 if len(v) >= 2 else len(v)):
            answer.append(v[j]['i'])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

