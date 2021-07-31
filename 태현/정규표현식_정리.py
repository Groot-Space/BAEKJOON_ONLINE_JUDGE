import re
'''
[] 표현
모든 예제는 text = 'hello world' 라는 문자열을 예로 들거임.
[abc] <- 괄호 안에 있는 문자들이 text안에 존재 하는지 확인하는 것
[a-c] = [abc] 로 아이픈을 사용해 표현 가능.

dot표현
a.b 는 a%b 형태로 a와 b사이에 어떤 문자열이 포함된 모든 패턴을 찾아주는 것
* 매치가 가능한 경우
aab
a0b ..등
*매치가 불가능한 경우
abc
aab

반복(*)
ca*t
caat, caaaat 등이 매치 가능.
0번 반복도 가능. -> ct도 가능하다는 뜻.

반복(+)
ca+t
위와는 다르게 0번 반복은 매칭되지 않음.

반복{숫자}
ca{2}t = a가 2번 반복되었을 때만 매칭 가능.

반복 ?
0회 또는 1회 반복되는 경우.
ab?c
'''
#실습 - match
text = 'hello world'
p = re.compile('[a-z]+')
m = p.match(text)
print(m)

text = '1hello world' #문자열 맨 앞에 1이 들어가서 매칭이 안됨. none 반환
p = re.compile('[a-z]+')
m = p.match(text)
print(m)

#실습 -search
text = '1hello world' #match와 다르게 앞에 매칭이 안되는 것이 들어가도 뒷부분을 검사해줌.
p = re.compile('[a-z]+')
m = p.search(text)
print(m)

#실습 - findall
text = '1hello world' #일치하는 문자열을 리스트에 담아서 리턴해 줌
p = re.compile('[a-z]+')
m = p.findall(text)
print(m)

#실습 - finditer #match 객체 반환
text = '1hello world'
p = re.compile('[a-z]+')
m = p.finditer(text)
for i in m:
    print(i)

'''
match 객체란 ?
.group() 매치된 문자열을 리턴한다.
.start() 매치된 문자열의 시작 위치를 리턴한다.
.end() 매치된 문자열의 끝 위치를 리턴한다.
.span() 매치된 문자열의 (시작, 끝)에 해당되는 튜플을 리턴한다.
'''
for i in m:
    print(i.group())
    print(i.start())
    print(i.end())
    print(i.span())