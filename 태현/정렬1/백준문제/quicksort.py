arr = [3,-8,1,-7,6,8,7,12]

def quicksort(arr,st, ed):
    if ed <= st + 1:
        return
    else:
        pivot = arr[st]
        l = st + 1
        r = ed - 1
        while True:
            while arr[l] <= pivot and l <= r:
                l += 1

            while arr[r] >= pivot and l <= r:
                r -= 1

            if l > r:
                break

            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp

        temp = arr[r]
        arr[r] = arr[st]
        arr[st] = temp

        quicksort(arr,st,r)
        quicksort(arr,r+1,ed)

        return

quicksort(arr,0, len(arr))

print(arr)