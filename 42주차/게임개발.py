n,m = map(int,input().split())
dx= [-1,0,1,0]
dy = [0,1,0,-1]
rx,ry,d = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
visited = [[0]*n for _ in range(n)]
visited[rx][ry] = 1
answer =1
while True:
    for _ in range(4):
        d= (d-1)%4
        nx = rx+dx[d]
        ny = ry+dy[d]
        if not visited[nx][ny] and g[nx][ny] == 0:
            visited[nx][ny] = 1
            rx,ry = nx,ny
            answer += 1
            break
    else:
        tmp = d
        tmp = (tmp+2)%4# 반대 방향 후진.
        rx += dx[tmp]
        ry += dy[tmp]
        if g[rx][ry] == 1:
            break
print(answer)
# 이코테 실전 연습 문제.
# 1: 바다, 0: 육지. 테두리는 바다로 둘러쌓임.
# 반시계 왼쪽 방향에 가본적이 없고, 바다가 아닌 칸이 있다면 전진.
# 만약 4방향 가능한 칸이 모두 없다면, 방향 유지한 채로, 한 칸 후진. 이 때 바다라면 종료