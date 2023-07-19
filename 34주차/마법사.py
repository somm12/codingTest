import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
water = []
for _ in range(n):
    water.append(list(map(int,input().split())))
answer = 0

cloud = [[False]* n for _ in range(n)]

cloud[n-1][0] =True
cloud[n-1][1] =True
cloud[n-2][0] =True
cloud[n-2][1] =True

def moveCloud():
    global cloud, d,s
    new = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if cloud[x][y]:
                nx = x
                ny = y
                for _ in range(s):
                    nx += dx[d]
                    ny += dy[d]
                nx %= n
                ny %= n
                new[nx][ny] = True
    cloud = new

def rain():
    global water
    for x in range(n):
        for y in range(n):
            if cloud[x][y]:
                water[x][y] += 1
# def removeCloud():
#     global cloud
#     arr = []
#     for x in range(n):
#         for y in range(n):
#             if cloud[x][y]:
#                 arr.append((x,y))
#                 cloud[x][y] = False
    

def magic():
    global water
    for x in range(n):
        for y in range(n):
            if cloud[x][y]:
                cnt = 0
                for i in [1,3,5,7]:
                    nx = x+dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if water[nx][ny] > 0:
                            cnt += 1
                water[x][y] += cnt

def makeCloud():
    global cloud,water
    new = [[False]*n for _ in range(n)] # 이 부분에서 이전 구름이 자동으로 삭제가 됨.
    for x in range(n):
        for y in range(n):
            if water[x][y] >= 2 and not cloud[x][y]:
                new[x][y] = True
                water[x][y] -= 2
    cloud = new

for _ in range(m):
    d,s = map(int,input().split())
    d -= 1
    moveCloud()
    rain()
    
    magic()
    makeCloud()


for x in range(n):
    for y in range(n):
        answer += water[x][y]
print(answer)