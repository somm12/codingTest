n,m = map(int,input().split())
r,c,d = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
cnt = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    if g[r][c] == 0:
        cnt += 1
        g[r][c] = 2# 청소 완료
    flag = True
    for i in range(4):
        nx = r+ dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:# 주변 4곳에 빈칸이 있다면
            flag= False
            d -= 1
            if d < 0:
                d = 3
            if g[r+dx[d]][c+dy[d]] == 0:#반시계 90도 회전 후 해당 방향으로 빈칸이 존재하면 전진.
                r += dx[d]
                c += dy[d]
            break
    if flag:# 빈칸이 없을 때 후진
        if d >=2:
            nx = r + dx[d-2]
            ny = c + dy[d-2]
        else:
            nx = r + dx[d+2]
            ny = c + dy[d+2]
        if g[nx][ny] == 1:# 후진 했을 때, 벽이라면 종료.
            break
        else:# 아니면 후진.
            r = nx
            c = ny

print(cnt)