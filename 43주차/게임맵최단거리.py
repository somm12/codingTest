from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        if x == n-1 and y == m-1:# 마지막 칸에 도착하면 칸 수 반환.
            return dist[x][y]+1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 벽, 격자 범위, 방문 여부.
            if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y]+1# 이전 칸에서 +1 만큼 이동.
    
    return -1# 마지막 칸에 도달을 못한다면 -1
# 프로그래머스 bfs.
# ** 출발 칸 포함 총 칸수를 구해야함!