n,m,k = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

g = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,m,s,d= map(int,input().split())
    g[x-1][y-1].append((m,s,d))


def move():
    global g

    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for m,s,d in g[x][y]:
                nx= (x+ (dx[d]*s))%n # 행과 열이 연결돼있어서 %n 필수.
                ny = (y + (dy[d]*s)) % n
                tmp[nx][ny].append((m,s,d))

    g = tmp

def makeOne():
    global g

    for x in range(n):
        for y in range(n):
            if len(g[x][y]) >= 2:
                tm,ts,d1,d2 = 0,0,0,0
                cnt = len(g[x][y])
                for m,s,d in g[x][y]:
                    tm += m
                    ts += s
                    if d % 2 == 0:# 방향이 상하좌우 중 하나
                        d1 += 1
                    else:
                        d2 += 1
                if tm // 5 > 0:# 방향이 대각선 중 하나.
                    g[x][y] = []
                    nm = tm//5
                    ns = ts//cnt
                    if d1 > 0 and d2> 0:# 각 방향이 모두 대각선, 모두 상하좌우 인 경우가 아닌, 섞인 경우라면, 대각선을 가짐.
                        for di in [1,3,5,7]:
                            g[x][y].append((nm,ns,di))
                    else:
                        for di in [0,2,4,6]:
                            g[x][y].append((nm,ns,di))
                else:# 질량이 0이면 소멸.
                    g[x][y] = []


for t in range(1,k+1):

    move()# 원자 이동

    makeOne()# 한 칸에 2개이상인 원자들 하나로 합성.
  

answer = 0
for x in range(n):
    for y in range(n):
        for m,_,_ in g[x][y]:
            answer += m
print(answer)
# 코드트리 원자충돌.