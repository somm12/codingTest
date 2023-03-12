def solution(dartResult):
    dict = {'S':1,'D':2,'T':3}
    arr = []
    cnt = 0
    for i in dartResult:
        if i in dict:
            cnt = 0
            arr[-1] = arr[-1]**dict[i]
        elif i == '*':
            cnt = 0
            arr[-1] = arr[-1]*2
            if len(arr) >= 2:
                arr[-2] = arr[-2] * 2
        elif i == '#':
            cnt = 0
            arr[-1] = arr[-1]*-1
        else:
            cnt += 1
            if cnt == 2:
                arr[-1] = 10
            else:
                arr.append(int(i))
    return sum(arr)
# 다트게임 - 복습