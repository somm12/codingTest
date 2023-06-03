n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = -1
dx= [-1,1,0,0]
dy = [0,0,-1,1]
def temp(x,y,i,visited,new): # 한 블록에 대해서 i 방향으로 쭉 이동.
    nx = x
    ny = y
  
    while True: # 범위 내, 또는 두 블록이 합쳐지거나, 다른 값인 블록을 만날 때까지 이동시킨다.
        nx += dx[i]
        ny += dy[i]
        
        if nx < 0 or nx >= n or ny <0 or ny >= n:
            new[nx-dx[i]][ny-dy[i]] = new[x][y]
            if x != nx-dx[i] or ny-dy[i] != y:
                new[x][y] = 0
            break
        if new[nx][ny] != 0: # 이동 중 해당 칸에 값이 있다면
            if not visited[nx][ny] and new[x][y] == new[nx][ny]: # 합쳐지지 X, 값이 같음.
                new[nx][ny] *= 2 # 두 배가 되고 원래자리는 0. 이미 합쳐 졌으니 1 할당
                new[x][y] = 0
                visited[nx][ny] = 1
                break
            else: # 다른 숫자라면 이동 하기 이전 칸에서 현재값을 할당하고, 원래 위치는 0을 할당.
                new[nx-dx[i]][ny-dy[i]] = new[x][y]
                if x != nx-dx[i] or ny-dy[i] != y: # **이동하기 전 후가 같다면 0을 할당X
                    new[x][y] = 0
                
                break
   
def move(arr):
    new = [[0]*n for _ in range(n)] # 한 경우에서 이동할 시, 다른 배열에 이동 결과를 담는다.
    # 원본 배열에 담으면 원본이 변형됨.
    for i in range(n):
        for j in range(n):
            new[i][j] = g[i][j]
    
    for i in arr:
        visited = [[0]*n for _ in range(n)] # 한 번 이동하는 동안만 이미 합쳐진것만 피함. 
        if i == 0: # 위쪽
            for y in range(n):
                for x in range(1,n):
                    
                    if new[x][y] != 0:
                        temp(x,y,i,visited,new)
        elif i == 1: # 아래쪽
            for y in range(n):
                for x in range(n-2,-1,-1):
                    if new[x][y] != 0:
                        temp(x,y,i,visited,new)
        elif i == 2: # 왼쪽
            for x in range(n):
                for y in range(1,n):
                    if new[x][y] != 0:
                        temp(x,y,i,visited,new)
        else:#우측.
            for x in range(n):
                for y in range(n-2,-1,-1):
                    if new[x][y] != 0:
                        temp(x,y,i,visited,new)
    a = -1
    # 하나의 이동 경우 최댓값 블록 반환.
    for i in range(n):
        for j in range(n):
            a = max(a,new[i][j])  
    
    return a              

def dfs(L,res): # 중복 순열을 이용한 전체 경우의 구하기. (상하좌우)
    global answer
    if L > 5: # 최대 5번 이동
        return
    # 최대 5번 이동으로 얻을 수 있는 최댓값찾기, 모든 경우 찾기.
    answer = max(answer,move(res))
    for i in range(4):
        dfs(L+1, res+[i])
dfs(0,[])

print(answer)