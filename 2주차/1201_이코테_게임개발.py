n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
cnt = 1
visited[x][y] = 1
turn_cnt = 0
dx = [-1,0,1,0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        visited[nx][ny] = 1
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
            turn_cnt = 0
        else:
            break
print(cnt)