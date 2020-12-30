def choose(spl, s):
    ret = []
    start = 0
    end = spl
    while end <= len(s):
        flag = 0
        flag2 = 0
        temp = s[start:end]

        for j in range(len(temp)-1):
            if temp[j] != temp[j+1]:
                flag2 += 1
                break

        if flag2 == 0 and spl != 1:
            start += 1
            end += 1
            continue
        if len(ret) != 0:

            for i in ret:
                if s[start:end] == i:
                    flag += 1
                    break
        if flag == 0:
            ret.append(s[start:end])
        start += 1
        end += 1
        if end > len(s): break
    return ret

def RLE(ret, s):
    result = []
    for i in range(len(ret)):
        st = ''
        count = 0
        start = 0
        end = len(ret[i])

        while end <= len(s):
            if s[start:end] == ret[i]:
                temp_start = start + len(ret[i])
                temp_end = end + len(ret[i])
                count += 1

                while end <= len(s):
                    if s[temp_start:temp_end] != ret[i]:
                        break
                    count += 1
                    temp_start += len(ret[i])
                    temp_end += len(ret[i])

                if count > 1 :
                    if len(ret[i])*count >= len(ret[i]) + 3:
                        st = s[:start] + str(count) + '(' + ret[i] + ')' + s[temp_end-len(ret[i]):]
                    break
                count = 0
            start += 1
            end += 1

        if len(st) != 0:
            result.append(st)


    if len(result) != 0:
        s_list = []
        m = len(result[0])
        for i in range(len(result)):
            if len(result[i]) <= m:
                s_list.append(result[i])
                m = len(result[i])
        return s_list

    else:
        return [s]
#메인
f = open('testcase.txt', 'r')
line = f.readline().rstrip()
line_list = [line]
ans = [len(line)]
for i in range(len(line)//2,0,-1):
    new_line = []
    for line in line_list:
        ret = choose(i, line)
        new_line += RLE(ret, line)
    line_list = new_line

m = len(line_list[0])
for line in line_list:
    if len(line) < m:
        m = len(line)

print(line_list)
print(m)
#     ans.append(len(line))
# ans.sort()
# print(ans[0])
