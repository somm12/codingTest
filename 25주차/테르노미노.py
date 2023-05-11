import sys
input = sys.stdin.readline
n,m = map(int,input().split())
g = []
max_val = -1 # 가장 큰 수를 담을 변수.
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        max_val = max(max_val,g[i][j])
answer = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 시간 복잡도: 500*500* 4^4(6천만 이상) * 3(덧셈계산) => 2억번 이상. 시간 초과 가능.
# 줄이기 위해서 가지 치기를 잘라야하므로, 현재 남은 개수 * 종위 위의 최댓값 이하면 return.
def dfs(x,y,total,cnt):
    global answer
    # '지금까지의 total + 남은 개수 * 최댓값' < answer 면 끝냄.
    if total + (4-cnt)*max_val <= answer: 
        return
    if cnt == 4: # 테르노미노 4개가 만들어지면 updates
        answer = max(answer,total)
        return
    
    for k in range(4):# 상 하 좌 우 방향으로 뻗어나가면서 테르로미노 만들기.
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 내이고, 아직 방문하지 않은 칸이라면 뻗어나가기.
        if 0 <= nx < n and 0<= ny < m and not visited[nx][ny]:
            # 두번째 테르노미노 칸일 때, ㅏ 모양의 경우를 만들기 위해 
            # 이어서 가지를 뻗어나가지않고 그대로 재귀를 이어나가서 만들 수 있음.
            if cnt == 2: 
                visited[nx][ny] =1
                dfs(x,y,total+g[nx][ny],cnt+1)
                visited[nx][ny] = 0
            # 다른 모양도 만들기 위해 방문처리하고 가지차기 이어나가기.
            visited[nx][ny] =1
            dfs(nx,ny,total+g[nx][ny],cnt+1)
            visited[nx][ny] = 0

visited = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 시작 칸 방문처리.
        visited[i][j] = 1
        dfs(i,j,g[i][j],1)
        visited[i][j] = 0
    
print(answer)