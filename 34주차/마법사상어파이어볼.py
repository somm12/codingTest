n,m,k = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
g = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    cr,cc,cm,cs,cd = map(int,input().split())
    g[cr-1][cc-1].append([cm,cs,cd])

def move():
    global g
    new =[[[] for _ in range(n)] for _ in range(n)]
    for x in range(n): # 모든 볼이 이동함.
        for y in range(n):
            if len(g[x][y]) >0:
                
                for idx in range(len(g[x][y])):
                    nx = x
                    ny = y
                    cm,cs,cd = g[x][y][idx]
                    for _ in range(cs):
                        nx += dx[cd]
                        ny += dy[cd]
                    nx %= n
                    ny %= n
                    new[nx][ny].append([cm,cs,cd])
    g=new

def divideBall():# 4개의 볼로 나누어짐. 2번째 조건.
    global g
    for x in range(n):
        for y in range(n):
            if len(g[x][y]) > 1:
                totalM = 0
                totalS = 0
                odd = 0
                even = 0
                length = len(g[x][y])
                for idx in range(len(g[x][y])):
                    cm,cs,cd = g[x][y][idx]
                    totalM += cm
                    totalS += cs
                    if cd % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if even == length or odd == length:
                    direct = [0,2,4,6]
                else:
                    direct = [1,3,5,7]
                
                g[x][y] = []
                if totalM//5:
                    for di in direct:
                        g[x][y].append([totalM//5, totalS//length, di])
for _ in range(k):
    move()
    divideBall()

answer = 0
for x in range(n):
    for y in range(n):
        if len(g[x][y]) > 0:
            for idx in range(len(g[x][y])):
                cm,cs,cd = g[x][y][idx]
                answer += cm
print(answer)

# 마법사 상어와 파이어볼- 배열만을 이용해서 구현해보기 version