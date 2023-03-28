def update(b,arr):
    n = len(b[0])
    m = len(b)
    for x,y in arr:
        b[x][y] = 0
    # 재배열하기
    new = [[0]*n for _ in range(m)]
    for j in range(n):
        s = []
        for i in range(m):
            if b[i][j] != 0:
                s.append(b[i][j])
        i = m -1
        while s:
            x = s.pop()
            new[i][j] = x
            i -= 1
    return new
    
                

def solution(m, n, board):
    answer = 0
    dict = {}
    dx = [0,1,1]
    dy = [1,0,1]
    board = [list(i) for i in board]
    while True:
        for x in range(m):
            for y in range(n):
                cnt = 1
                for i in range(3):
                    nx = x + dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < m and 0 <= ny < n and board[x][y] == board[nx][ny] and board[x][y] != 0:
                        cnt += 1
                    if cnt == 4:
                        dict[(x,y)] = 1
                        for i in range(3):
                            nx = x + dx[i]
                            ny = y +dy[i]
                            dict[(nx,ny)] = 1
        if len(dict) == 0:
            break
        answer += len(dict)
        board = update(board,dict.keys())
        dict = {}
            
    return answer
# 프렌즈4블록