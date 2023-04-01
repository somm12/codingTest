from collections import deque
def solution(row, col, queries):
    answer = []
    g = [[0]*col for _ in range(row)]
    s = 1
    for i in range(row):
        for j in range(col):
            g[i][j] = s
            s += 1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for x1,y1,x2,y2 in queries:
        nx = x1 - 1
        ny = y1 - 1
        idx = deque()
        v = deque()
        d = [y2-y1,x2-x1]
        
        for i in range(4):
            for _ in range(d[i%2]):
                nx += dx[i]
                ny += dy[i]
                idx.append((nx,ny))
                v.append(g[nx][ny])
        answer.append(min(v))
        v.rotate(2)
        idx.rotate(1)
        for x,y in idx:
            g[x][y] = v.popleft()
        
    return answer
# 행렬 테두리 회전하기