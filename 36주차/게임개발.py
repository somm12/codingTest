n,m = map(int,input().split())
rx,ry,d = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx= [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0# 탐색 횟수 세는 변수.
visited = [[0]* m for _ in range(n)]
answer =0
while True:
    if cnt == 4:# 4방향 모두 이미 바다 or 가본칸이라면,
        nx = rx+dx[(d-2)%4]
        ny = ry+dy[(d-2)%4]# 후진.
        if g[nx][ny] == 1:# 바다가 있다면 멈춤.
            break
        else:
            rx,ry = nx,ny# 후진이 가능하다면 위치 업데이트. 다시 방향 탐색 횟수는 0
            cnt = 0 
    # 왼쪽 방향 회전.   
    di = (d-1)%4
    nx = rx+dx[di]
    ny = ry +dy[di]
    # 왼쪽방향에 아직 가보지 않은 칸 존재할시, 전진하고 방향 회전.
    if not visited[nx][ny] and g[nx][ny] == 0:
        d = di
        cnt =0
        rx,ry = nx,ny
        answer += 1
        visited[nx][ny] =1
        continue
    else: # 존재하지 않으면 회전만.
        d = di
    cnt += 1
print(answer)