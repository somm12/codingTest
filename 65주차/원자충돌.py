n,M,k = map(int,input().split())
info = {}

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(M):
    x,y,m,s,d = map(int,input().split())
    x -= 1
    y -= 1
    if (x,y) in info:
        info[(x,y)].append([m,s,d])
    else:
        info[(x,y)] = [[m,s,d]]

def move():
   
    global info
    tmp = {}
    for x,y in info:

        for m,s,d in info[(x,y)]:
            
            nx,ny = (x+(dx[d]*s))%n, (y+ (dy[d] * s))% n # 다음 이동할 방향.
            
            if (nx,ny) in tmp:
                tmp[(nx,ny)].append([m,s,d])
            else:
                tmp[(nx,ny)] = [[m,s,d]]
            
    info = tmp

def combination():
    global info
    tmp = {}
    for x,y in info:
        if len(info[(x,y)]) >= 2:# 한칸에 2개이상이면 결합
            cnt = len(info[(x,y)])
            totalS, totalM, cross,di = 0,0,0,0
            for m,s,d in info[(x,y)]:
                totalS += s
                totalM += m
                if d % 2 == 0:
                    di += 1
                else:
                    cross += 1
            nm = totalM // 5

            if nm > 0:
                ns = totalS // cnt 
                tmp[(x,y)] = []
                if cross > 0 and di > 0:# 대각선, 상하좌우 방향 골고루 있다면
                    for nd in [1,3,5,7]: # 대각선 방향 지정.
                        tmp[(x,y)].append([nm,ns,nd])
                else:
                    for nd in [0,2,4,6]:
                        tmp[(x,y)].append([nm,ns,nd])
        else:
            tmp[(x,y)] = info[(x,y)]
    
    info = tmp


for _ in range(k):
    move()# 이동
    
    combination()# 결합

answer = 0
for key in info:
    for m,s,d in info[key]:
        answer += m  
print(answer)
