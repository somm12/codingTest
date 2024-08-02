n = int(input())
dx = [-1,1,0,0]# 상 하 좌 우.
dy = [0,0,-1,1]
answer =0
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))


def dfs(L,board):
    global answer
    if L == 5:      
        for v in board:
            answer = max(answer,max(v))
        return
    for i in range(4):
        visited = [[0]*n for _ in range(n)]
        tmp = [[0]*n for _ in range(n)]
        if i == 0:
            for y in range(n):
                pos = 0
                for x in range(n):
                    if visited[x][y] or board[x][y] == 0: continue
                    tmp[pos][y] = board[x][y]# 한 방향으로 이동 후에, 옮겨질 위치. (중력 작용.)
                    for k in range(x+1,n):# 단, 그 뒤에 값에서 같은 값이 있다면 2배로 만들고 방문 처리. 하지만 그 뒤에서 0이 아닌 가장 가까운 값이 다른 값이면 break.
                        if board[x][y] == board[k][y]:
                            tmp[pos][y] *= 2
                            visited[x][y] = 1
                            visited[k][y] = 1
                            break
                        elif board[k][y] != 0: break
                    pos += 1
            dfs(L+1,tmp)
        elif i == 1:
            for y in range(n):
                pos = n-1
                for x in range(n-1,-1,-1):
                    if visited[x][y] or board[x][y] == 0: continue
                    tmp[pos][y] = board[x][y]
                    for k in range(x-1,-1,-1):
                        if board[x][y] == board[k][y]:
                            tmp[pos][y] *= 2
                            visited[x][y] = 1
                            visited[k][y] = 1
                            break
                        elif board[k][y] != 0: break
                    pos -= 1
            dfs(L+1,tmp)
    
        elif i == 2:
            for x in range(n):
                pos = 0
                for y in range(n):
                    if visited[x][y] or board[x][y] == 0: continue
                    tmp[x][pos] = board[x][y]
                    for k in range(y+1,n):
                        if board[x][y] == board[x][k]:
                            tmp[x][pos] *= 2
                            visited[x][y] = 1
                            visited[x][k] = 1
                            break
                        elif board[x][k] != 0: break
                    pos += 1
            dfs(L+1,tmp)
        elif i == 3:
            for x in range(n):
                pos = n-1
                for y in range(n-1,-1,-1):
                    if visited[x][y] or board[x][y] == 0: continue
                    tmp[x][pos] = board[x][y]
                    for k in range(y-1,-1,-1):
                        if board[x][y] == board[x][k]:
                            tmp[x][pos] *= 2
                            visited[x][y] = 1
                            visited[x][k] = 1
                            break
                        elif board[x][k] != 0: break
                    pos -= 1
            dfs(L+1,tmp)
dfs(0,g)
print(answer)