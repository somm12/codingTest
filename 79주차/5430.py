from collections import deque
T  = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    arr =arr[1:-1]
    if (len(arr) > 0):
        arr = list(arr.split(","))# split를 하면 배열에 원소가 빈 문자가 한개 생겨버림. 유의 
    
    arr = deque(arr)
    cnt = 0
    
    for s in p:
        if s == 'R':
            cnt += 1
        else:
            if len(arr) == 0:
                print("error")
                break
            if cnt %2 == 1:
                arr.pop()
            else:
                arr.popleft()
    else:# 중간에 break가 안된 상태일때.
        if cnt % 2 == 0:# 뒤집기 짝수번 해서 그대로인 형태.
            arr = ','.join(arr)
            print("[" + arr + "]")
        else:# 뒤집기 홀수번 해서 거꾸로인 형태.
            arr.reverse()
            arr = ','.join(arr)
            print("[" + arr + "]")
