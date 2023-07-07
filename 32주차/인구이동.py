from collections import deque
n,L,R= map(int,input().split())
country = []
for _ in range(n):
    country.append(list(map(int,input().split())))

days = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def makeUnit(x,y):# x,y 위치를 시작점으로 연합국가 찾기.
    global visited
    q = deque()
    q.append((x,y))
    visited[x][y] =1
    unit = [(x,y)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(country[x][y] - country[nx][ny]) <= R:# 인구수 차이가 L, R 사이라면
                    unit.append((nx,ny))# 연합 국가에 append
                    q.append((nx,ny))# 이어서 연합국가를 찾기위해 append
                    visited[nx][ny] = 1 # 방문처리
    return unit

def movePeople(): # 인구 이동 시작.
    global country,united
    for unit in united:
        total = 0
        length = len(unit)
        for x,y in unit:
            total += country[x][y]
        for x,y in unit:
            country[x][y] = total//length
        

while True:# 더이상 인구 이동이 이뤄지지 않을 때 까지 반복.
    visited = [[0]*n for _ in range(n)] # 매 인구 이동 마다, 방문 여부 표시.
    united = []# n번째 인구 이동 때, 만들어진 연합 국가.
    for x in range(n):
        for y in range(n):
            if not visited[x][y]: # 방문하지 않은 국가에 대해서 연합을 구한다.
                unit = makeUnit(x,y) # 연합 구하기.
                if len(unit) > 1: # 자기 자신을 제외해서 연합이 구해지면, append.
                    united.append(unit)
    if len(united) == 0: # 연합이 만들어 지지 않는다면, 인구이동X-> 종료.
        break
    movePeople()# 인구 이동.
    days += 1
print(days)
