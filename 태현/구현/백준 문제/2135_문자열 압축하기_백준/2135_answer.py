from sys import stdin as f

def sumation(text, condition):
    start, end, length = condition
    count = (end - start + 1) // length
    text = text[:start] + str(count) + '(' + text[start:start + length] + ')' + text[end + 1:]
    return text


def find(text, word_len):
    length = len(text) - word_len
    count = 0
    condition = []
    check = False
    for loc in range(length):
        if text[loc] == text[loc + word_len] and text[loc] != '(' and text[loc] != ')':
            count += 1
            if count % word_len == 0:
                if not check:
                    start = loc - word_len + 1
                check = True
                condition = [start, start + count + word_len - 1, word_len]
        else:
            if check:
                text = sumation(text, condition)
                return text, True
    if check:
        text = sumation(text, condition)
        return text, True
    return text, False


def solution(text):
    word_len = len(text) // 2
    while word_len > 0:
        text, condition = find(text, word_len)

        if condition:
            continue

        if len(text) < word_len:
            word_len = len(text) // 2
        else:
            word_len -= 1
    return text
f = open('testcase.txt','r')
line = f.readline().rstrip()
length = len(line)
ans = len(solution(line))
if ans >= length:
    print(length)
else :
    print(ans)
