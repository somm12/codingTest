from collections import deque
dx = [-1,1,0,0]
dy= [0,0,-1,1]
answer = "IMPOSSIBLE"
R,C = map(int,input().split())
jh = deque()
fire = deque()

visited = [[0]*C for _ in range(R)]# 지훈의 방문처리 배열
g = []
for i in range(R):
    g.append(list(input()))
    for j in range(C):
        if g[i][j] == "J":
            visited[i][j] = 1
            jh.append((i,j,0))
        elif g[i][j] == "F":
            fire.append((i,j,0))

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

def go():
    global answer
    time = 0# 매 분마다 불, 지훈이 이동 현황을 실행.
    while len(jh) > 0:
        while len(fire) > 0 and fire[0][2] <= time:
            x,y,ft = fire.popleft()
            for i in range(4):
                nx,ny = x + dx[i], y + dy[i]
                if inRange(nx,ny) and g[nx][ny] != "#" and g[nx][ny] != "F":# 벽을 제외한 이미 방문하지 않은 곳으로 불이 퍼짐.
                    g[nx][ny] = "F"
                    fire.append((nx,ny, ft+1))
        while len(jh) > 0 and jh[0][2] <= time:
            x,y,jt = jh.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y +dy[i]
                if not inRange(nx,ny):# 가장자리에 닿는 것 == 범위를 벗어남 => 탈출.
                    answer = jt + 1
                    return 
                if g[nx][ny] =="." and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    jh.append((nx,ny,jt+ 1))
        time += 1# 1분 지남.

go()
print(answer)
# 백준 불!