'''
대문자 / 특수기호 / 띄어쓰기 제거 정규 표현식
'''

s = ['가나다다나가']

import re
str = str.lower()
str = re.sub('[^a-z0-9]', '', str) #str 에서 알파벳과 숫자를 찾아서 없애줌


