from collections import deque

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def inRange(x,y):
    return 0<= x < n and 0 <= y < n
def makeGroup():# 그룹 만들기 [[(0,0),(0,1)],[],,]
    gr = []
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = 1
                gr.append(bfs(x,y,visited))
    return gr

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    v = g[x][y]
    one = [(x,y)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and not visited[nx][ny] and g[nx][ny] == v:
                visited[nx][ny] = 1
                one.append((nx,ny))
                q.append((nx,ny))

    return one

def combi():# 그룹 조합.
    tmp = []
    m = len(group)
    def comb(start,res):
        if len(res) == 2:
            tmp.append(res)
            return
        for i in range(start,m):
            comb(i+1,res+[i])
    comb(0,[])
    return tmp

def find(g1,g2):# 맞닿은 변수의 구하기
    cnt = 0
    x,y = g2[0]
    v = g[x][y]

    for x,y in g1:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if inRange(nx,ny) and  (nx,ny) in g2:
                cnt += 1
                
        
    return cnt

def rotate():# 회전
    global g
    newG = [[0]*n for _ in range(n)]
    for y in range(n):
        newG[n-1-y][n//2] = g[n//2][y]
    for x in range(n):
        newG[n//2][x] = g[x][n//2]
    L = n//2
    for sx,sy in [(0,0),(0,n//2+1),(n//2+1,0),(n//2+1,n//2+1)]:
        for x in range(L):
            for y in range(L):
                newG[sx+y][sy+ L-1-x] = g[sx+x][sy+y]
    g= newG

for num in range(4):
    group = makeGroup()
    arr = combi()
    total = 0
    for a,b in arr:
        score = (len(group[a])+len(group[b]))
        x1,y1= group[a][0]
        x2,y2 = group[b][0]
        score *= (g[x1][y1]*g[x2][y2])
        close = find(group[a],group[b])# 맞닿은 변의 수 구하기
        score *= close
        total += score
    
    
    rotate()
    answer += total # n회차 점수
    
print(answer)
# 맞닿은 변의 수는 방문처리 필요 없음.
# 그룹은 다르지만, 색은 같을 수도.