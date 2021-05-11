def solution(numbers):
    nums = []
    ans = []
    for i in numbers:
        nums.append(i)
    ret = []
    isused = [0 for i in range(len(nums))]
    count = 0
    # print(nums)
    temp = makenums(nums, ret, count, isused)
    print(temp)


def makenums(nums, ret, count, isused):
    if count == len(nums):
        return ret
    else:
        for i in range(len(nums)):
            if isused[i] == 0:
                # print(nums[i])
                # if nums[i] != None:
                # print(ret)
                ret.append(nums[i])
                isused[i] = 1
                count += 1
                ret = makenums(nums, ret, count, isused)
                isused[i] = 0
                count -= 1
        return ret
solution("17")