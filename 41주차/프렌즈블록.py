def solution(m,n,board):
    answer = 0
    t = []
    for s in board:
        t.append(list(s))
    board = t # 배열 형태로 바꾸기. 문자열 형태라면 값을 바꿀 수 없음.

    while True:
        flag = False# 더이상 팡! 할 것이 없는지 확인.
        arr =[] # 팡! 이 될 수 있는 좌표(2x2 중 왼쪽 상단 좌표 한개)를 담은 배열.
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] == board[x][y+1] == board[x+1][y]== board[x+1][y+1] != '0':
                    arr.append((x,y))
                    flag = True # 터질 것이 있으므로 True
        
        for x,y in arr: # 터지는 부분 0으로 할당.
            board[x][y] = '0'
            board[x+1][y] = '0'
            board[x][y+1] = '0'
            board[x+1][y+1] = '0'
        # 아래로 당기기.
        # 최대 m번, 바로 한칸 밑에 빈칸과 바꾸는 방식으로 아래로 당기기.
        for _ in range(m):  
            for x in range(m-1): # 현재 row 밑에 칸에 빈칸이라면, 바로 아래칸과 값 바꾸기.
                for y in range(n):
                    if board[x+1][y] == '0':
                        board[x+1][y],board[x][y] = board[x][y],board[x+1][y]
                        
                        
        if not flag:# 더이상 터질게 없다면 break
            break
    for v in board:
        answer += v.count('0') # 0이 된 부분 개수 세기
    return answer
# 프로그래머스 카카오 문제
    