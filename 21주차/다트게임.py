def solution(dartResult):
    answer = 0
    arr = []
    dict = {'S':1,'D':2,'T':3}
    dartResult = dartResult.replace('10','A')
    
    for i in dartResult:
        if i.isdecimal():
            arr.append(int(i))
        elif i == 'A':
            arr.append(10)
        elif i in dict:
            arr[-1] = arr[-1] ** (dict[i])
        elif i == '*':
            arr[-1] *= 2
            if len(arr) > 1:
                arr[-2] *= 2
        elif i == '#':
            arr[-1] *= -1
    return sum(arr)