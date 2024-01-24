from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
L,N,Q = map(int,input().split())
chess =[]
scope = {}
scopeMap = [[0]*L for _ in range(L)]
info = {}#체력
answer = {}


for _ in range(L):
    chess.append(list(map(int,input().split())))
for i in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    r -= 1
    c -= 1
    scope[i] = []
    answer[i] = 0
    for x in range(r,r+h):
        for y in range(c,c+w):
            scopeMap[x][y] = i
            scope[i].append((x,y))
    info[i] = k

def inRange(x,y):
    return 0 <= x < L and 0 <= y < L

def demage(arr):
    global answer, scope, scopeMap, info
    for num in arr:
        cnt = 0
        for x,y in scope[num]:
            if chess[x][y] == 1:
                cnt += 1
        if cnt > 0:
            answer[num] += cnt
        if info[num] - cnt <= 0:
            for x,y in scope[num]:
                scopeMap[x][y] = 0
            del scope[num]
            del info[num]
            del answer[num]
        else:
            info[num] -= cnt
            

def move(nth,d):
    global scopeMap, scope
    q = deque()
    q.append(nth)
    arr = []
    while q:
        num = q.popleft()
        arr.append(num)
        tmp = set()
        for x,y in scope[num]:
            nx,ny = x+dx[d],y+dy[d]
            if not inRange(nx,ny) or chess[nx][ny] == 2:# 벽 만나면 종료.
                return []
            if scopeMap[nx][ny] > 0 and scopeMap[nx][ny] != num: # 다른 기사가 있으면
                tmp.add(scopeMap[nx][ny])
        for v in tmp:# 겹치는 기사도 이동.
            q.append(v)
    newMap = [[0]*L for _ in range(L)]
    for num in arr:# 이동 시키기.
        a = []
        for x,y in scope[num]:
            nx,ny = x+dx[d],y+dy[d]
            newMap[nx][ny] = num
            a.append((nx,ny))
        scope[num] = a
    for num in scope:
        if num not in arr:# 이동하지 않는 기사.
            for x,y in scope[num]:
                newMap[x][y] = num

    scopeMap = newMap
    return arr

    
for _ in range(Q):
    nth,d = map(int,input().split())
    if nth not in scope:
        continue
    arr = move(nth,d)# 이동한 기사들.
  
    if len(arr) > 1:
        demage(arr[1:])# 젤 처음 이동한 즉, 명령 받은 기사 제외.

    
total = 0

for v in answer:
    total += answer[v]
print(total)
# info[num] = 체력 # 기사들 체력.
# scope[num] = [좌표들] # 기사들이 속한 좌표.
# scopeMap => 그래프에 기사들 번호 넣기.
