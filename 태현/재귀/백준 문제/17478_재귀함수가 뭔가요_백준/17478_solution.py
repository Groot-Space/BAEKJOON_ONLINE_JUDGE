n = int(input())
k = 0
under_bar = "____"
zero_line = '''"재귀함수가 뭔가요?"'''
first_line = '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'''
second_line = '''마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'''
third_line = '''그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
fourth_line = '''"재귀함수는 자기 자신을 호출하는 함수라네"'''
fifth_line = '''라고 답변하였지.'''
sentences = [zero_line,first_line,second_line,third_line,fourth_line,fifth_line]
def recursive_def(n, k, under_bar,sentences):
    if n == k:
        print(under_bar * k + sentences[0])
        print(under_bar * k + sentences[4])
        print(under_bar * k + sentences[5])
        return
    else :
        print(under_bar * k + sentences[0])
        print(under_bar * k + sentences[1])
        print(under_bar * k + sentences[2])
        print(under_bar * k + sentences[3])
        recursive_def(n,k+1,under_bar,sentences)
        print(under_bar * k +sentences[5])

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursive_def(n,k,under_bar,sentences)