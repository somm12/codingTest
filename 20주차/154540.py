from collections import deque
def bfs(g,visited,x,y):
    q= deque()
    q.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 1
    cnt = int(g[x][y])
    n = len(g)
    m = len(g[0])
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y +dy[i]
            if 0 <= nx < n and 0<=ny < m and g[nx][ny] != 'X':
                if not visited[nx][ny]:
                    cnt += int(g[nx][ny])
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return cnt
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    food = []
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                food.append((i,j))
    if len(food) == 0:
        return [-1]
    for i,j in food:
        if not visited[i][j]:
            cnt = bfs(maps,visited,i,j)
            answer.append(cnt)
  
    answer.sort()
    return answer
# 무인도 여행