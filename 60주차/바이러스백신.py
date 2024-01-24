from collections import deque
n,m = map(int,input().split())
g = []
hos = []
answer= int(1e9)
dx= [-1,1,0,0]
dy = [0,0,-1,1]
hosLen = 0
virus = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 2:
            hos.append([i,j])
            hosLen += 1
        if g[i][j] == 0:
            virus += 1

def combination():
    arr = []
    def dfs(start, res):
        if len(res) == m:
            arr.append(res)
            return
        for i in range(start,hosLen):
            dfs(i+1, res+[i])
    dfs(0,[])
    return arr

def inRange(x,y):
    return 0<= x < n and 0 <= y < n
def bfs(q):
    
    visited =[[0]*n for _ in range(n)]
    remain = virus
    for i,j,t in q:
        visited[i][j] = 1
   
    while q:
        x,y,t = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] != 1 and not visited[nx][ny]:
                if g[nx][ny] == 0:
                    remain -= 1
                    if remain == 0:
                        return t+1
                q.append((nx,ny,t+1))
                visited[nx][ny] = 1
    
    
    return -1

combi = combination()
if virus == 0:
    print(0)
else:
    for idxs in combi:
        q = deque()
        for i in idxs:
            q.append(hos[i]+[0])
        
        time = bfs(q)# 걸린 시간
        
        if time < 0:# 바이러스 모두 소멸이 안되는 경우는 pass.
            continue
        else:
            answer = min(answer,time)
    

    if answer == int(1e9):
        print(-1)
    else:
        print(answer)