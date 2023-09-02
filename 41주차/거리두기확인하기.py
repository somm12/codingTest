from collections import deque
def bfs(x,y,board):
    q = deque()
    q.append((x,y,0))
    visited = [[0]*5 for _ in range(5)]
    visited[x][y] = 1
    dx =[-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        x,y,dist = q.popleft()
        if dist >= 2:
            continue
        for i in range(4):
            nx = x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < 5 and 0<= ny < 5 and not visited[nx][ny]:
                if board[nx][ny] == 'X':
                    continue
                elif board[nx][ny] == 'P':
                    return False
                else:
                    q.append((nx,ny,dist+1))
                    visited[nx][ny] = 1
    return True
            
def solution(places):
    answer = []
    for board in places:
        arr = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'P':
                    arr.append((i,j))
        for i,j in arr:
            if bfs(i,j,board):
                continue
            else:
                answer.append(0)
                break
        else:
            answer.append(1)
        
    return answer
# 한 명이라도 거리두기가 안되어 있다면 break.