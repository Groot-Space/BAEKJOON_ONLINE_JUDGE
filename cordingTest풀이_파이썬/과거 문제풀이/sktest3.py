#!폰 북을 정렬한다.
# 첫번 째 요소를 !pivot에 팝.
# pivot 글자 길이를 구함. !pivotlen
# 각 요소를 포문으로 돌린다.
# 돌린 포문의 글자를 피봇 길이만큼 컷한다.
# 피봇과 비교해서 일치하면 false
# 끝까지 다 돌아서 일치하지 않으면 false
def solution(phone_book):
    arr = []
    phone_book = quicksort(phone_book)
    for i in phone_book:
        if type(i) != str:
            arr.append(str(i))
        else:
            arr.append(i)

    for j in range(0, len(arr)):
        length = len(arr[j])
        for k in range(j+1, len(arr)):
            if arr[j] == arr[k][:length]:
                return False
    return True
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    small_arr, equal_arr, greater_arr = [], [], []
    for i in arr:
        if i < pivot:
            small_arr.append(i)
        elif i == pivot:
            equal_arr.append(i)
        else:
            greater_arr.append(i)
    return quicksort(small_arr) + equal_arr + quicksort(greater_arr)

#print(solution(["119", "97674223", "1195524421"]))
#print(solution(["123", "456", "789"]))
print(solution(["12","123","1235","567","88"]))