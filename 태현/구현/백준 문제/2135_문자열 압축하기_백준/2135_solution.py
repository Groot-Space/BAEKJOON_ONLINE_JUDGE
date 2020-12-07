f = open('testcase.txt', 'r')
line = f.readline().rstrip()

arr1 = []
arr3 = []
maxinterval = len(line) // 2

#단어 묶음별 분할
for i in range(2,maxinterval):
    start = 0
    end = i
    arr2 = []
    while True:
        if end > len(line):
            break

        else:
            arr2.append([start,0,line[start:end]])

        start += 1
        end += 1
    arr1.append(arr2)

#중복횟수 카운트
interval = 1
for j in arr1:
    interval += 1

    for k in j:
        start = 0
        end = interval

        # print(k)
        while True:
            if end > len(line):
                break

            elif k[2] == line[start:end]:
                k[1] += 1

            # print(k[2]," : ",line[start:end])
            start += 1
            end += 1

        if k[1] > 1:
            if len(arr3) != 0:
                flag = 0
                for l in arr3:
                    if l[2] == k[2]:
                        flag += 1
                if flag == 0:
                    arr3.append(k)
            else:
                arr3.append(k)

def sort(arr):
    front = 0
    mid = len(arr) //2
    end = len(arr)-1

    while True:
        if front == end:
            return arr
        elif arr[front][1] < arr[mid][1]:
            temp = arr[front]
            arr[front] = arr[mid]
            arr[mid] = temp


#결과확인
for l in arr3:
    print(l)