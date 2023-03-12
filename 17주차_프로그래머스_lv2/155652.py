def solution(s,skip,index):
    ans = ''
    arr =[]
    dict = {}
    idx = 0
    for i in range(97,123):
        tmp = chr(i)
        if tmp not in skip:
            dict[tmp] = idx
            arr.append(tmp)
            idx += 1
    for i in s:
        next = dict[i] + index
        if next >= len(arr):
            ans += arr[next%len(arr)]
        else:
            ans += arr[next]
    return ans
# 둘만의 암호 - 복습














