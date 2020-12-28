def makestring(l,s):
    s = s[:l[0]] + str(l[1]) + l[2] + s[l[3]:]
    return s
def RLE(s_split,s):
    start = 0
    end = s_split
    while end <= len(s):
        cri = s[start:end]
        count = 1
        com_start = end
        com_end = end + s_split
        while com_end <= len(s):
            if cri == s[com_start:com_end]:
                count += 1
                com_start += s_split
                com_end += s_split
            elif count > 1 or (count > 1 and com_end <= len(s)):
                s = makestring([start,count,cri,com_end-s_split],s)
                break
            else:
                break
        start += s_split
        end += s_split

    return len(s), s
#메인
f = open('testcase.txt', 'r')
line = f.readline().rstrip()
ret = [[len(line),line]]
for i in range(1,len(line)//2):
    length, s = RLE(i,ret[-1][1])
    print(s)
    ret.append([length,s])