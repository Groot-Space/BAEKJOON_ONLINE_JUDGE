# from collections import deque
#
# def solution(n, k, cmd):
#     cur = k
#     arr = [0 for i in range(n)]
#     leng = len(arr) - 1
#     m = deque()
#
#     for cm in cmd:
#         c = cm.split()
#         if c[0] == 'C':
#             arr[cur] = 1
#             m.appendleft(cur)
#             if cur < leng:
#                 cur += arr[cur]
#             else :
#                 cur -= 1
#         elif c[0] == 'D':
#             for i in range(int(c[1])):
#                 cur += 1
#                 cur += arr[cur]
#         elif c[0] == 'U':
#             for i in range(int(c[1])):
#                 cur -= 1
#                 cur -= arr[cur]
#         elif c[0] == 'Z':
#             z = m.popleft()
#             arr[z] = 0
#     answer = ''
#     for i in arr:
#         if i == 0:
#             answer += "0"
#         else :
#             answer += "X"
#     print(answer)
#
#
# cmd = ["U 13", "C", "D 13", "C", "Z", "Z","U_1","U 13", "C", "D 13", "C", "Z", "Z","U_1"]
# solution(20, 15, cmd)
