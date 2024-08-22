from collections import deque
dx = [-1,1,0, 0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
g = []
virus =[]
empty = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(n):
        if g[i][j] == 2:
            virus.append((i,j))
        if g[i][j] == 0:
            empty += 1
            
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def choose():
    result = []
    def dfs(start,res):
        if len(res) == m:
            result.append(res)
            return 
        
        for i in range(start, len(virus)):
            dfs(i+1,res + [virus[i]])
            
    dfs(0,[])
    
    return result
    

def spread(pos):
    q = deque()
    visited =[[0]*n for _ in range(n)]
    
    for x,y in pos:
        q.append((x,y))
        visited[x][y] = 1
    
    remain = empty
    time = 0
    while q:
        length = len(q)# 각 초 시간대 까지만 pop하고, 시간 흐름을 나타낸다.
         
        if remain == 0:# 빈칸이 모두 바이러스로 채워지는 순간.
            return time 
        time += 1
        for _ in range(length):
            x,y= q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] != 1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if g[nx][ny] == 0:# 만약 빈칸이면 개수 -1.
                        remain -= 1
                        
                
    return int(1e9)# 빈칸을 모두 채우지 못한경우.
            

answer = int(1e9)

arr = choose()

for a in arr:
    
    answer = min(answer,spread(a))# m개 활성화 후, 퍼졌을 때, 걸린시간.

if answer == int(1e9):# 결국 빈칸이 항상 채워질 수 없다면 -1
    print(-1)
else:
    print(answer)
# 백준 연구소3