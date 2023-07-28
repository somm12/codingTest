from collections import deque
n,m,fuel = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

tx,ty = map(int,input().split())
tx -=1
ty -= 1
dict = {}
for _ in range(m):
    a,b,c,d = map(int,input().split())
    dict[(a-1,b-1)]= (c-1,d-1)

def choose():# 탑승자 고르기.
    q = deque()
    q.append((0,tx,ty))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1

    cand = []# 손님이 있는 곳까지 이동시 거리와 출발지, 도착지 좌표를 담을! 즉 후보들을 담는 배열.
    while q:
        dist,x, y = q.popleft()
        if (x,y) in dict:# 이동한 좌표 x,y가 dict에 포함된 좌표라면(출발지라면! 즉 손님이 있는 곳)
            ex,ey = dict[(x,y)]
            cand.append((dist,x,y,ex,ey))
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx <n and 0 <= ny< n and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] =1
                q.append((dist+1,nx,ny))
    
    cand.sort(key=lambda x:(x[0],x[1],x[2]))# 거리가 작고, 행, 열이 작은순.
    if len(cand) != len(dict) or cand[0][0] > fuel:# 모두 이동시킬 수 없는 경우(벽때문에 접근 불가) or 연료보다 멀다면, -1
        return -1
    return cand[0]# 출발지로 이동 가능하다면, 선택된 탑승자 반환.

def goDestination(ex,ey):# 손님을 데리고 도착지로 이동시키기.
    q = deque()
    q.append((0,tx,ty))
    visited = [[0]*n for _ in range(n)]
    visited[tx][ty] = 1

    while q:
        dist,x, y = q.popleft()
        if x == ex and y == ey: # 도착지점으로 갔다면 거리반환.
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx <n and 0 <= ny< n and not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] =1
                q.append((dist+1,nx,ny))
    return -1# 이 경우는 도착지로 갈 수 없는 상황이므로, -1 반환.


while True:
    if len(dict)==0:# 손님이 모두 이동했다면 남은 연료반환.
        print(fuel)
        break

    cand = choose()# 태울 손님 선택

    if cand == -1:# 중간에 연료 소모 또는 모두 이동할 수 없다면 종료.
        print(-1)
        break
    dist,sx,sy,ex,ey = cand # 출발지로 이동할 때 거리, 출발지 도착지 변수에 담기
    fuel -= dist # 연료 소모
    tx,ty = sx,sy # 택시 좌표 이동.

    dist =goDestination(ex,ey)# 도착지로 이동.
    if dist == -1 or dist > fuel: # 중간에 연료 소모 또는 접근할 수 없는 상황.
        print(-1)
        break
    fuel -= dist # 도착지 까지 연료소모
    fuel += (dist*2)# 도착하면 거리*2 만큰 충전
    tx,ty = ex,ey# 택시 위치 업데이트

    del dict[(sx,sy)]# 한명 이동시켰으므로, dict에서 제거.
# 모두 이동할 수 없는 경우, 연료가 중간에 소모되는 경우 체크.