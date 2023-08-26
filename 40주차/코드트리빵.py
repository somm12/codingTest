from collections import deque

n,m = map(int,input().split())
done = [0]*(m+1)

g = []
people = {}# 사람들 번호에 따른 위치 ex) {1: (1,0),,}
destination = {}# 번호에 따른 편의점 위치 {1: (5,0), 2:(3,4),,}
dx = [-1,0,0,1]
dy = [0,-1,1,0]# 상 좌 우 하
active = [[1]*n for _ in range(n)]# 갈 수 없는 좌표 표시.
for _ in range(n):
    g.append(list(map(int,input().split())))

for i in range(1,m+1):
    ex,ey = map(int,input().split())
    destination[i] = [ex-1,ey-1]

def isFinish():# m 명 모두 도착했는지 확인.
    for i in range(1,m+1):
        if done[i] == 0:
            return False
    return True

def move():# 이동. 격자에 있는 모든 사람들이 편의점 까지 최단 거기로 이동할 수 있는! 인접한 1칸으로 이동.
    # 최단 거리 경로를 구해야함.
    global people
    if len(people) == 0:
        return
    
    newPeople= {}# 이동하면서 새로 좌표가 바뀐 정보를 넣을 딕셔너리.
    for num in people:
        x,y = people[num]# 현재 위치
        ex,ey = destination[num]# 목적지 위치
        if not done[num]:# 아직 편의점에 도착하지 않은 사람 중에서
            q = deque()
            q.append((x,y,0,[]))
            visited = [[0]*n for _  in range(n)]
            visited[x][y] = 1
            cand = []
            while q:
                x,y,dist,route= q.popleft()
                if x == ex and y == ey:# 도착 위치에 도달하면, 후보자 배열에 추가.
                    cand.append((dist,route[0]))
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0 <= nx < n and 0 <= ny <n and active[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] =1
                        q.append((nx,ny,dist+1,route+[(nx,ny)]))# 최단 경로 위치 추가.
            cand.sort(key=lambda x:x[0])# 가장 경로가 짧은 곳을 중심으로 정렬.
            nextX, nextY = cand[0][1]# 다음 이동할 칸 선택.
            newPeople[num] = (nextX,nextY)
    
    people = newPeople# 사람들 좌표 정보 업데이트.

def isArrive():#도착했다면 해당칸은 못지나가도록 이를 처리하는 함수.
    global done, active

    for num in people:
        x,y = people[num]# 현재 사람의 위치
        ex,ey = destination[num]# 목표 위치.
        if x == ex and y == ey:
            active[x][y] = 0 # 못지나감 표시.
            done[num] = 1 # 이동 완료 표시.

def baseCamp(): #편의점에서 가까운 베이스 캠프로 이동.
    global active

    cand = []# 후보
    ex,ey = destination[t] # 원하는 편의점 위치.
    q = deque()
    q.append((ex,ey,0))
    
    visited = [[0]*n for _ in range(n)]
    visited[ex][ey] = 1
    
    while q:
        x,y, dist = q.popleft()
        if g[x][y] == 1:#베이스 캠프 라면,  상 좌 우 하 순으로 탐색하므로 자동으로, 행과 열이 작은 부분 부터 탐색됨.
            sx,sy = x,y
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and active[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny,dist+1))
    
   

    active[sx][sy] = 0 # 이제 도착한 베이스 캠프 해당 칸 못지나감.
    people[t] = (sx,sy) # t번째 사람이 이동함.


t = 1
while True:
    move()# 이동
    isArrive()# 도착 했는지 확인
  
    if t <= m:# 베이스 캠프로 이동
        baseCamp()
      
    if isFinish(): # 모두 도착했는지 확인
        break
    t += 1
print(t)
# 코드 트리 삼성 기출