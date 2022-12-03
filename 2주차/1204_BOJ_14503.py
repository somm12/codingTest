
n, m = map(int, input().split())
r, c, d = map(int, input().split())
visited = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
area = []
turn_time = 0
for _ in range(n):
    area.append(list(map(int ,input().split())))
visited[r][c] = 1
cnt = 1
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    if area[nx][ny] == 0 and visited[nx][ny] == 0:
        r = nx
        c = ny
        cnt += 1
        visited[r][c] = 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if area[nx][ny] == 0:
            r = nx
            c = ny
            turn_time = 0
            continue
        else:
            break
print(cnt)