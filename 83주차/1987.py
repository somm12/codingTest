
n,m  = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(input()))
dx =[ -1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0 <= x < n and 0 <= y < m
def bfs(x,y):
  
    q= set()
    q.add((x,y,1,g[x][y]))# 같은 좌표에 다른 루트로 도달했더라도 현재까지 지나온 알파벳이 같다면 같은 경우이므로, set을 이용해서 중복 제거!!
    answer = 1
    while q:
        x,y,cnt,route = q.pop()
        for i in range(4):
            nx,ny = x +dx[i],y+dy[i]
            if inRange(nx,ny) and g[nx][ny] not in route:
                q.add((nx,ny,cnt+1,route+g[nx][ny]))
                answer = max(cnt+1, answer)
        
             
    return answer
print(bfs(0,0))
# 백준 알파벳.
