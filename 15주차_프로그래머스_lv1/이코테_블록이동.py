from collections import deque
def get_next(p,board):
    res = []
    p = list(p)
    x1 = p[0][0]
    y1 = p[0][1]
    x2 = p[1][0]
    y2 = p[1][1]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        nx1 = dx[i] + x1
        ny1 = dy[i] + y1
        nx2 = dx[i] + x2
        ny2 = dy[i] + y2
        
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            res.append({(nx1,ny1),(nx2,ny2)})
    if x1== x2:
        for i in [-1,1]:
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                res.append({(x1,y1),(x2+i,y1)})
                res.append({(x2,y2),(x1+i,y2)})
                
    elif y1 == y2: 
        for i in [-1,1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                res.append({(x2,y1+i),(x2,y2)})
                res.append({(x1,y1),(x1,y2+i)})
    return res
def solution(board):
    n = len(board)
    new = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new[i+1][j+1] = board[i][j]
    q = deque([])
    pos = {(1,1),(1,2)}
    q.append((pos,0))
    visited = []
    visited.append(pos)
    while q:
        p, cost = q.popleft()
        if (n,n) in p:
            return cost
        for next in get_next(p,new):
            if next not in visited:
                q.append((next, cost+1))
                visited.append(next)
# 블록이동 복습.
# {(1,1)(1,2)} == {(1,2)(1,1)} 로 처리하기 위해서 집합 연산자 set사용.