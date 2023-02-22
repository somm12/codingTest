import sys
import copy
input = sys.stdin.readline
graph = []
ans = 0
n,m = map(int,input().split())
can = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            can.append((i,j))
length = len(can)
def spread(x,y,g):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if g[nx][ny] == 0:
            g[nx][ny] = 2
            spread(nx,ny,g)
def area(g):
    res = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                res += 1

    return res

# for c in list(combinations(can,3)):
#     g = copy.deepcopy(graph)
#     for i, j in c:
#         g[i][j] = 1
#     for k in range(n):
#         for t in range(m):
#             if g[k][t] == 2:
#                 spread(k,t,g)
#     ans = max(ans, area(g))

selected= []
def dfs(L,s):
    global ans
    if L == 3:
        g = copy.deepcopy(graph)
        for i,j in selected:
            g[i][j] = 1
        for k in range(n):
            for t in range(m):
                if g[k][t] == 2:
                    spread(k,t,g)
        ans = max(ans, area(g))
        return
    for i in range(s,length):
        selected.append(can[i])
        dfs(L+1,i+1)
        selected.pop()  
dfs(0,0)
print(ans)
        