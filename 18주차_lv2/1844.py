def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = []
    q.append((0,0))
    while q:
        x,y = q.pop(0)
        if x == n-1 and y == m-1:
            return maps[n-1][m-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                if visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    
    return -1
# 게임 맵 최단거리