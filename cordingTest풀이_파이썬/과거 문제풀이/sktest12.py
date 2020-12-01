def solution(numbers, target):
    cnt = 0
    def operator(numbers, target, idx=0): #첫루틴 2두번째 루틴 3마지막 루틴
        if idx < len(numbers): #1. idx = 0, idx = 1, 2, 3, .....   , idx = len(nubers)
            numbers[idx] *= 1 #[1,1,1]
            operator(numbers, target, idx+1)
            # 0[1,1,1] -> 밑에 단계가 끝나면 더하기 후 종료
            #     1[1,1,1] -> 밑에 단계가 끝나면 더하기 후 종료
            #         2[1,1,1] -> 더하기 후 종료
            #         2[1,1,-1]
            #     1[-1,1,1]
            #
            # 0[-1,1,1]
            #     1[-1,1,1]
            #     1[-1,-1,1]

            numbers[idx] *= -1 # [-1,1,1,1,1]
            operator(numbers, target, idx+1)# 2.[-1,1,1,1,1]

        elif sum(numbers) == target: #위에서
            nonlocal cnt
            cnt += 1

    operator(numbers, target)
    return cnt