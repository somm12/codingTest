from collections import deque
def getPos(pos,board): # 현재 위치에서 이동가능한 위치 반환해주는 함수.
    pos = list(pos) # pos는 set 자료형으로, list으로 바꿔줌.
    
    x1,y1 = pos[0] # 각 좌표
    x2,y2 = pos[1]
    
    res = []# 이동 가능한 좌표를 담을 배열.
    dx = [-1,1,0,0]# 상 하 좌 우
    dy = [0,0,-1,1]
    
    for i in range(4):# 상 하 좌 우 방향으로 움직일 수 있는지 체크.
        nx1 = x1+dx[i]
        ny1 = y1+dy[i]
        nx2 = x2+dx[i]
        ny2 = y2+dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            res.append({(nx1,ny1),(nx2,ny2)}) # 두 좌표 모두 빈칸이라면 추가.
    
    # 회전 구간
    if x1 == x2:# 가로 모양일 때 ( 위 아래 쪽으로 회전)
        for d in [1,-1]:# 회전할 때 축의 대각선 부분과 회전을 했을 때의 칸이 모두 빈칸인지 체크.
            if board[x1+d][y1] == 0 and board[x2+d][y2] == 0:
                
                res.append({(x1,y1),(x1+d,y1)})
                res.append({(x2,y2),(x2+d,y2)})
    
    if y1 == y2:# 세로 모양일 때 ( 오른쪽 왼쪽으로 회전)
        for d in [1,-1]:
            if board[x1][y1+d] == 0 and board[x2][y2+d] == 0:
                
                res.append({(x1,y1),(x1,y1+d)})
                res.append({(x2,y2),(x2,y2+d)})
    return res

def solution(board):
    answer = 0
    n = len(board) 
    # 범위를 벗어났을 때의 범위 확인 부분을 좀 더 수월하게 하기 위해서 board의 테두리 모두 1로 채움.
    newBoard = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]
    
    visited = [{(1,1),(1,2)}] # 시작점 방문처리. (1,2),(1,1)도 같은 좌표이므로, 중복을 없애기 위해서 set형태로 두기.
    q= deque()
    q.append([{(1,1),(1,2)}, 0])# 현재 위치와 현재까지의 거리를 묶어서 큐에 넣기.
    while q:
        pos, dist= q.popleft()
        if (n,n) in pos:
            return dist
        for nextPos in getPos(pos,newBoard):
            if nextPos not in visited:
                q.append([nextPos, dist+1])
                visited.append(nextPos)
                    
                        
    return answer
# 프로그래머스 카카오문제