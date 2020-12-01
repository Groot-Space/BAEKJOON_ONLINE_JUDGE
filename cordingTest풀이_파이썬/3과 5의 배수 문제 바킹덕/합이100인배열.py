def func(List, n):
    n = len(List)
    for i in range(n):
        for j in range(i+1, n):
            _temp = List[i] + List[j]
            if _temp == 100:
                return 1
            