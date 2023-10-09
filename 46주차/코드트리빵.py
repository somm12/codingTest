from collections import deque
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
desti = {}# 목적지 => {1: [x,y], 2:[],,,,,}
for i in range(1,m+1):# m명의 각 가고싶은 편의점 위치 입력 
    x,y = map(int,input().split())
    desti[i] = [x-1,y-1]
people = {}# 사람 위치
time = 1
cnt = m
able = [[1]*n for _ in range(n)]# 이동 가능한 칸인지 여부를 나타내는 2차원 배열. 1로 이동 가능하도록 초기화
dx = [-1,0,0,1]# 상 좌 우 하
dy = [0,-1,1,0]
def inRange(x,y):# 범위 내에 해당하는지 확인하는 함수
    return 0 <= x < n and 0 <= y < n
def move():# 격자에 있는 모든 사람이 편의점 방향으로 이동.
    global people
    newPeople = {} # 사람들의 변경된 위치를 담을 딕셔너리.
    for num in people:
        x,y = people[num]
        tx,ty = desti[num]
        q = deque()
        q.append((x,y,[(x,y)]))
        visited = [[0]*n for _ in range(n)]
        visited[x][y]= 1
        while q:
            x,y,route = q.popleft() # 이동할 수 있는 칸으로만 최단 거리로 이동할 수 있는 칸으로 1칸 이동.
            if [x,y] == [tx,ty]:
                nextX,nextY = route[1] # 다음 칸으로 이동.
                newPeople[num] = [nextX, nextY] # 해당 사람의 위치 변경.
                break
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny] and able[nx][ny] == 1:
                    q.append((nx,ny,route+[(nx,ny)]))
                    visited[nx][ny] = 1
    people = newPeople # 위치 업데이트.

def isArrive():# 이동 한 후, 편의점에 도착 했다면 해당 칸으로 더이상 지나갈 수 없음. 모두가 도착했다면 True반환.
    global able, people, cnt
    newPeople = {}
    for num in people:
        x,y = people[num]
        tx,ty = desti[num]
        if [x,y] == [tx,ty]:# 도착했다면 딕셔너리에 넣기 않기. ( 완료 처리 )
            able[tx][ty] = 0
            cnt -= 1 # 1명 도착했으므로, cnt 1 감소.
        else:# 편의점에 도착하지 않았다면, 새로운 딕셔너리에 넣기.
            newPeople[num] = [x,y]
    people= newPeople
    return cnt == 0

def baseCamp():# t <=m일 때, t번 사람이 베이스 캠프로 이동. t번이 가려고 하는 편의점에서 최단거리, 행,열이 작은 순.
    global people, able

    x,y = desti[time]
    cand = []# 베이스 캠프 후보
    q= deque()
    q.append((x,y,0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,dist = q.popleft()
        if g[x][y] == 1:# 베이스 캠프 도착시,
            cand.append((dist,x,y))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and able[nx][ny] == 1:
                q.append((nx,ny,dist+1))
                visited[nx][ny] =1
    cand.sort(key =lambda x:(x[0],x[1],x[2]))
    a,b = cand[0][1], cand[0][2] # 이동할 베이스 캠프 좌표
    people[time] = [a,b]# 베이스 캠프로 이동
    able[a][b] = 0# 해당 칸은 이동 불가.


while True:

    if len(people) > 0:
        move()
    if isArrive(): # 편의점 도착 후 처리, 모두가 편의점에 도착했다면 True반환 후 종료.
        break

    if time <= m:
        baseCamp()

    time += 1
print(time)


# 삼성 기출.