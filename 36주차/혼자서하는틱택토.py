def count(board):
    a = 0
    b = 0
    for arr in board:
        for v in arr:
            if v == 'O':
                a += 1
            elif v == 'X':
                b += 1
    return (a,b)

def isWin(s, board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == s:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == s:
            return True
    if board[0][0] == board[1][1] == board[2][2]== s:
        return True
    if board[0][2] == board[1][1] == board[2][0]== s:
        return True
    return False

def solution(board):

    first,next = count(board)
    if abs(first - next) > 1 or first < next:# 번갈아서 진행
        return 0
    if isWin('O',board) and next >= first:# 선공이 승리
        return 0
    
    if isWin('X',board) and first != next:# 후공이 승리
        return 0
    return 1
# 프로그래머스 lv2