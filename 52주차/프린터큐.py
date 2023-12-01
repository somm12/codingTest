from collections import deque
T = int(input())

for _ in range(T):
    n, targetIdx = map(int,input().split())
    cnt  =1
    arr = list(map(int,input().split()))
    q = deque()
    for i,v in enumerate(arr):
        q.append([v,i])
    while q:
        now, idx =q.popleft()
        for v in q:
            if now < v[0]:# 하나라도 큰 값이 있다면, 다시 큐 뒤에 추가.
                q.append([now,idx])
                break
        else:# 한번도 큰 값이 없었다면, 큐에서 빠져나옴. 그 때의 idx가 찾으려는 순서라면 print하기.
            if idx == targetIdx:
                print(cnt)
                break
            cnt += 1
# 백준 큐 자료구조 문제