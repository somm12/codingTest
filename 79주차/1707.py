import sys
input = sys.stdin.readline
n = int(input()) 
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
arr = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(res):
    if len(res) == 5:
        arr.append(res)
        return
    for i in range(4):
        dfs(res+[i])
dfs([])

answer = 0
def inRange(x,y):
    return 0 <= x< n and 0 <= y < n
def move():
    for _ in range(n):#중력 적용.
        for x in range(n):
            for y in range(n):
                if tmp[x][y] > 0 :
                    
                    nx,ny= x+dx[d],y+dy[d]
                    if inRange(nx,ny) and tmp[nx][ny] == 0:
                        tmp[x][y],tmp[nx][ny]= tmp[nx][ny], tmp[x][y]

def collision():
    if d % 2 == 0:# 상 또는 좌 방향.
        for x in range(n):
            for y in range(n):
                if tmp[x][y] > 0:
                    nx,ny = x+dx[d],y+dy[d]
                    if inRange(nx,ny) and tmp[nx][ny] == tmp[x][y]:
                        tmp[nx][ny] += tmp[x][y]
                        tmp[x][y] = 0
    else:# 하 또는 우 방향.
        for x in range(n-1,-1,-1):
            for y in range(n-1,-1,-1):
                if tmp[x][y] > 0:
                    nx,ny = x+dx[d],y+dy[d]
                    if inRange(nx,ny) and tmp[nx][ny] == tmp[x][y]:
                        tmp[nx][ny] += tmp[x][y]
                        tmp[x][y] = 0

for di in arr:
    tmp = [a[:] for a in g]
    for d in di:
        move()# 이동
        collision()# 충돌.
        move()#  다시 이동.
    for a in tmp:
        answer = max(answer,max(a))

print(answer)