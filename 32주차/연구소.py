from collections import deque
import copy
n,m = map(int,input().split())

board = []

empty = []
virus = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = -1

for i in range(n):
    board.append(list(map(int,input().split())))
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i,j))
        elif board[i][j] == 2:
            virus.append((i,j))

def spread(res): # 바이러스 퍼짐.
    tmp = copy.deepcopy(board)
    q = deque(virus)
    for i,j in res:
        tmp[i][j] = 1

    visited = [[0]*m for _ in range(n)]
    for i,j in virus:
        visited[i][j] =1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] =2
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    return tmp
def area(tmp):# 안전 영역 구하기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

def wall(L,res,start): # 벽 세개 설치. - 조합
    global answer
    if L == 3:
        tmp = spread(res)
        answer = max(answer,area(tmp))
        return

    for i in range(start,len(empty)):
        wall(L+1, res+[empty[i]],i+1)

wall(0,[],0)
print(answer)

