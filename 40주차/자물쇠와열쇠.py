import copy
def solution(key,lock):
    answer = False
    n = len(lock)
    m = len(key)
    board = [[0]*(3*n) for _ in range(3*n)]# 자물쇠를 한 가운데 위치 시키기 위한 격자판.
    for i in range(n):
        for j in range(n):
            board[n+i][n+j] = lock[i][j]# 자물쇠 두기.
    
    def rotate(key):# 열쇠 회전.
        new = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                new[j][m-1-i] = key[i][j]
        return new
    
    def check():# 현재 자물쇠 부분의 홈이 열쇠의 돌기와 정확히 들어맞는지 확인.
        for i in range(n):
            for j in range(n):
                if board[n+i][n+j] != 1:
                    return False
                
        return True
                
    for _ in range(4):# 90도 회전하여 총 4방향 회전 가능
        key = rotate(key)
        for x in range(2*n): # 0에서 2*n 만큼 행 이동
            for y in range(2*n): # 0에서 2*n 만큼 열 이동. 한 칸씩 이동하면서
                
                for i in range(m): # 격자판과 key의 합을 구하기
                    for j in range(m):
                        board[x+i][y+j] += key[i][j]
                        
                if check(x,y):# 이 때 자물쇠 부분이 열쇠와 맞는지 체크하기
                    return True
                    
                for i in range(m):# 아니라면 원래 격자판으로 다시 되돌리기.
                    for j in range(m):
                        board[x+i][y+j] -= key[i][j]
            
    return answer
# 프로그래머스 카카오 기출.