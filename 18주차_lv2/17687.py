def trans(x,n):
    a = []
    if x == 0:
        return ['0']
    while x != 0:
        tmp = x % n
        if tmp >= 10:
            tmp = hex(tmp)[-1].upper()
        a.append(str(tmp))
        x = x//n
    return a[::-1]
def solution(n, t, m, p):
    answer = ''
    s = 0
    arr = []
    
    while len(arr) < t*m:
        v = trans(s,n)
        for i in v:
            arr.append(i)
        s += 1
    last = t*m
   
    return ''.join(arr[p-1:last:m])
# n진수 게임