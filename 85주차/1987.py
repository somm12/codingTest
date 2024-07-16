R,C = map(int,input().split())
g = []
for _ in range(R):
    g.append(list(input()))

def inRange(x,y):
    return 0 <= x < R and 0 <= y < C

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer =0
visited = [0]*26
def bfs(x,y):
    global answer
    s = set()# set을 이용하여, 특정 지점 까지 올 수 있는 경우에서 같은 경우를 제외 시킬 수 있음. 2,2 까지 오는 경우 중 ABC,ABC 여러가지 가능.
    s.add((x,y,g[x][y]))
    while len(s)>0:
        x,y,alpha= s.pop()
        if len(alpha) == 26:
            return 26
        answer = max(answer,len(alpha))
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] not in alpha:# 이미 존재하는 알파벳으로는 이동 불가.
                tmp= alpha + g[nx][ny]
                s.add((nx,ny,tmp))
                
    return answer

def dfs(x,y,cnt):
    global answer
    answer = max(cnt,answer)
    if cnt == 26:
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if inRange(nx,ny):
            tmp = ord(g[nx][ny]) - 65
            if not visited[tmp]:
                visited[tmp] = 1 # 이전에 방문한 알파벳으로는 재방문 불가.
                dfs(nx,ny,cnt+1)
                visited[tmp] = 0
# print(bfs(0,0))


first = ord(g[0][0])-65
visited[first] = 1
answer = 0
dfs(0,0,1)
print(answer)

# 최대 26. 완전탐색 또는 bfs 가능.