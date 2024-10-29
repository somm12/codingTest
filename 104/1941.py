from collections import deque
dx = [-1,1,0,0]# 상 하 좌 우.
dy = [0,0,-1,1]

def check():# 인접하는지 체크.
    
    visited = [[1]*5 for _ in range(5)]
    for x,y in arr: # 현재 고른 좌표는 0으로 셋팅.
        visited[x][y] = 0
    q= deque()
    sx,sy = arr[0]
    q.append((sx,sy))
    visited[sx][sy]=1
    total = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))
                total += 1 # 인접한 부분이라는 의미이므로 1개 증가.

    return total == 7
                

    
def dfs(L,start,cnt):# 25개 중 7개 중복 없이 조합.
    global answer
    if cnt >=4:# 임도연파가 더 많으면 안됌.
        return
    if L == 7:
        if check():# 모두 인접하면 +1
            answer += 1
        return 

    for i in range(start,25):
        r = i // 5 # 행
        c = i % 5 # 열
        arr.append((r,c))
        dfs(L+1,i+1, cnt + (g[r][c] == 'Y'))# 다음 조합.
        arr.pop()
g = []
for _ in range(5):
    g.append(list(input()))
answer = 0
arr =[]
dfs(0,0,0)
print(answer)
# 백준 소문난 칠공주.