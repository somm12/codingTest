n, m = map(int,input().split())
water = []
dx = [0,-1,-1,-1,0,1,1,1]# 8가지 방향 이동
dy = [-1,-1,0,1,1,1,0,-1]
cloud = [[0]*n for _ in range(n)]
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1
for _ in range(n):
    water.append(list(map(int,input().split())))

def move():# 구름 이동
    global cloud
    new = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if cloud[x][y] == 1:
                nx = x
                ny = y
                for _ in range(s):# s칸 만큼 이동.
                    nx += dx[d-1]
                    ny += dy[d-1]
                # 이동 후, 인덱스로 맞추기 위해 %n,
                # 음수일 때 +n 을 하여 index out of range 에러 방지.
                nx = nx % n
                ny = ny % n
                if nx < 0:
                    nx += n
                if ny < 0:
                    ny += n
                new[nx][ny] = 1
    cloud = new # 구름의 이동으로 새로운 배열을 다시 할당
def rain():# 물의 양 + 1
    global water
    for x in range(n):
        for y in range(n):
            if cloud[x][y] == 1:
                water[x][y] += 1

def magic():# 마법으로 대각선 방향에 물이 있는 바구니 개수 만큼 물의 양 증가.
    global water
    rx = [-1,-1,1,1]
    ry = [-1,1,-1,1]
    for x in range(n):
        for y in range(n):
            if cloud[x][y] == 1:
                for k in range(4):
                    nx = x + rx[k]
                    ny = y + ry[k]
                    if 0 <= nx < n and 0<= ny < n:
                        if water[nx][ny] > 0:# 대각선 방향에 물이 있는 바구니라면
                            water[x][y] += 1
                
def makeCloud():# 이전의 구름 외에 물의 양이 2이상이면, 구름을 생성.
    global water,cloud
    new = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if cloud[x][y] == 0 and water[x][y] >= 2:
                new[x][y] = 1
                water[x][y] -= 2
    cloud = new # 새로 구름이 생성되고 다시 할당

for _ in range(m):
    d,s = map(int,input().split())
    move()
    rain()
    magic()
    makeCloud()

answer = 0
# 최종 물의 양의 합.
for i in range(n):
    for j in range(n):
        answer += water[i][j]
print(answer)