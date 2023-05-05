

string = ["O","R","O","N","D","O","N","T","I","S","S"]
search =  ["N","T","I"]

def fail_func(string):
    j = 0
    arr = [0 for i in range(string)]
    for i in range(1,len(string)):
        while j > 0 and string[i] != string[j]:
            if string[i] == string[j] : arr[i] = j + 1
    return arr

