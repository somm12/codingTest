import sys
sys.setrecursionlimit(100000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

n,L,R = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

def inRange(x,y):
    return 0 <=x < n and 0<= y <n

# def bfs(x,y):
#     q= deque()
#     q.append((x,y))
#     visited[x][y]  =1
#     ret = []
#     while q:
#         x,y = q.popleft()
#         ret.append((x,y))
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if inRange(nx,ny) and not visited[nx][ny] and L <= abs(g[x][y] - g[nx][ny]) <= R:
#                 visited[nx][ny] = 1
#                 q.append((nx,ny))
#     return ret 

def dfs(x,y):# dfs로 인구이동 가능한 면적 찾기.
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny) and not visited[nx][ny] and L <= abs(g[x][y] - g[nx][ny]) <= R:
            visited[nx][ny] = 1
            ret.append((nx,ny))
            dfs(nx,ny)


while True:
    visited = [[0]*n for _ in range(n)]# 방문 처리 초기화.
    flag = False
    for x in range(n):
        for y in range(n):
            ret = []
            if not visited[x][y]:
                visited[x][y]= 1
                ret.append((x,y))
                dfs(x,y)

                if len(ret) >= 2:# 인구이동 발생.
                    flag = True
                    totalSum = sum([g[i][j] for i,j in ret])
                    value = totalSum//len(ret)
                    for i,j in ret:
                        g[i][j] = value
    if not flag:# 인구이동이 더이상 생기지 않음
        break
   
    answer += 1

print(answer)
# 백준 인구이동