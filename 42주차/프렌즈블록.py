import copy

def remove(r,c,board):# 2x2 같은 블록은 0으로 할당.
    newBoard = copy.deepcopy(board)
    res = set()
    for i in range(r-1):
        for j in range(c-1):
            if board[i][j] != 0:# 0이 아닌것 중에서.
                # 모두 같다면, 0을 넣고, set에 넣기.(중복된 좌표 제외)
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    newBoard[i][j] = 0
                    newBoard[i+1][j] = 0
                    newBoard[i][j+1] = 0
                    newBoard[i+1][j+1] = 0
                    res.add((i,j))
                    res.add((i,j+1))
                    res.add((i+1,j))
                    res.add((i+1,j+1))
    
    return [newBoard, len(res)]# 바뀐 형태와, 없어진 블록개수 반환
def clean(r,c,board):# 0 을 다시 위로 보내주기
    
    for j in range(c):
        for _ in range(r-1):# 위 아래로 바꾸는 대신, 빈칸이 한칸만 올라가므로, 행의 개수 만큼 반복.
            for i in range(r-1):
                if board[i+1][j] == 0:
                    board[i][j],board[i+1][j] = board[i+1][j], board[i][j]
                
    
def solution(m,n,board):
    answer = 0
    # m 은 행, n은 열
    tmp = []
    for v in board:
        tmp.append(list(v))
    board = tmp
    while True:
        newBoard, cnt = remove(m,n,board)
        if cnt == 0:# 더이상 없앨 블록이 없으면 끝.
            break
        board = newBoard
        clean(m,n,board)
        
        answer += cnt
    return answer
    # 프로그래머스 카카오문제