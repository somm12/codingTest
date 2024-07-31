from collections import deque

tc = int(input())
for _ in range(tc):
    func = input()
    n = int(input())
    arr = input()
    arr = arr[1:-1]
    if len(arr) > 0:
        arr = arr.split(",")
    rCnt = 0
    dCnt = 0
    q = deque(arr)
    flag = True
    for c in func:
        if c == 'R':
            rCnt += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                flag = False
                break
            elif rCnt % 2 == 1:
                q.pop()
            elif rCnt % 2 == 0:
                q.popleft()
    
    if flag:
        if rCnt % 2 ==1:
           q.reverse()
        arr = ','.join(q)
        print('[' + arr + ']')
# 백준 AC 문제.
# 매번 뒤집지 않고, 개수를 세어서 홀수번 일 때는 pop을 한다.