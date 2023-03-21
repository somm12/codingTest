import copy
n,m = map(int,input().split())
graph = []
cctv_list = []
answer = int(1e9)
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] in [1,2,3,4,5]:
            cctv_list.append((i,j,graph[i][j]))
cctv_type = [[],[[0],[1],[2],[3]],[[0,1],[2,3]],[[0,2],[0,3],[1,2],[1,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(L,graph):
    global answer
    if L == len(cctv_list):
        answer = min(area(graph),answer)
        return 
    tmp = copy.deepcopy(graph)
    x,y,type = cctv_list[L]
    for d in cctv_type[type]:
        watch(x,y,d,tmp)
        dfs(L+1,tmp)
        tmp = copy.deepcopy(graph)
def watch(x,y,d,graph):
    for i in d:
        nx,ny = x,y
        while True:
            nx += direction[i][0]
            ny += direction[i][1]
            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 6:
                    break
                if graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            else:
                break

def area(g):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1
    return cnt    

dfs(0, graph)
print(answer)
# 각 cctv 종류에서 될 수 있는 모든 방향의 조합을 따져가며, 감시 가능 영역을 계산하고
# cctv개수까지 조합이 생기면 (dfs 종료조건), 그에 따라 사각지대 (0의 개수)를 구함.
# dfs를 이용하는 것이 포인트.