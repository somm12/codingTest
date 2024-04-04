n,m,k = map(int,input().split())
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

info = {}
for _ in range(m):
    x,y,m,s,d = map(int,input().split())
    info[(x-1,y-1)] = [[m,s,d]]

def move():
    global info
    tmp = {}
    for x,y in info:
        for m,s,d in info[(x,y)]:
            nx = (x+ (dx[d]*s)) % n
            ny = (y+ (dy[d]*s)) % n
            if (nx,ny) in tmp:
                tmp[(nx,ny)].append([m,s,d])
            else:
                tmp[(nx,ny)] = [[m,s,d]]
    info = tmp

def combination():
    global info

    tmp = {}
    for x,y in info:
        if len(info[(x,y)]) >= 2:# 한 칸에 2개이상 일때만 원자들이 합쳐짐.
            tm,ts,cnt = 0,0, len(info[(x,y)])
            d1,d2 = 0,0 # 상하좌우 방향 개수, 대각선 개수
            for m,s,d in info[(x,y)]:
                tm += m
                ts += s
                if d % 2 == 0:
                    d1 += 1
                else:
                    d2 += 1
            if tm // 5 > 0:# 질량이 0되면 소멸
                xm = tm//5
                xs = ts//cnt
                tmp[(x,y)] = []
                if d1 > 0 and d2 > 0:# 모두 상하좌우 방향 이나 대각선이 아니라면, 4방향 대각선으로 나뉨.
                    for nd in [1,3,5,7]:
                        tmp[(x,y)].append([xm,xs,nd])
                else:
                    for nd in [0,2,4,6]:
                        tmp[(x,y)].append([xm,xs,nd])

        else:
            tmp[(x,y)] = info[(x,y)]
    info = tmp

for nth in range(1,k+1):
    if len(info) == 0:
        break
    move()
    
    combination()
   
answer = 0
for x,y in info:
    for m,s,d in info[(x,y)]:
        answer += m

print(answer)