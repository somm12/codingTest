from collections import deque


def next_position(board,pos):
    pos = list(pos)
    x1 = pos[0][0]
    y1 = pos[0][1]
    x2 = pos[1][0]
    y2 = pos[1][1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    res = []
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            res.append({(nx1,ny1),(nx2,ny2)})
    if x1 == x2:
        for i in [-1,1]:
            if board[x1+i][y1] == 0 and board[x1+i][y2] == 0:
                res.append({(x1+i,y2),(x2,y2)})
                res.append({(x1,y1),(x1+i,y1)})
    elif y1 == y2:
        for i in [-1,1]:
            if board[x1][y1+i] == 0 and board[x2][y1+i] == 0:
                res.append({(x1,y1+i),(x1,y1)})
                res.append({(x2,y1+i),(x2,y2)})
    return res
def solution(board):
    n = len(board)
    new = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new[i+1][j+1] = board[i][j]
    pos = {(1,1),(1,2)}
    visited = [pos]
    q = deque()
    q.append((0,pos))
    while q:
        cost, pos = q.popleft()
        if (n,n) in pos:
            return cost
        for next in next_position(new,pos):
            if next not in visited:
                q.append((cost+1,next))
                visited.append(next)
    return 0

# pos 변수를 집합 객체로 둬서 일일이 좌표를 나열하지 않아도 됨.
# 또한 집합 객체(set)을 사용함으로써 (1,1),(1,2) 와 (1,2),(1,1) 를 같은 것으로 보고 중복처리를 안함.