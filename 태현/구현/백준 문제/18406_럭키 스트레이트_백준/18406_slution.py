f = open('testcase.txt','r')
line = f.readline().rstrip()
left = line[:len(line)//2]
right = line[len(line)//2:]
sum = [0,0]

for i in range(len(left)):
    sum[0] += int(left[i])
    sum[1] += int(right[i])

if sum[0] == sum[1]:
    print('LUCKY')
else:
    print('READY')