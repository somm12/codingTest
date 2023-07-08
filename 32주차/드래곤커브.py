n = int(input())
board = {}

dy = [0,-1,0,1]
dx = [1,0,-1,0]
def startCurve(x,y,d,g):
    global board
    board[(x,y)] = 1 # 격자판에 시작점 표시.
    curve = [d] # 현재 커브의 방향 초기화.
    location = [(x,y)] # 만들어질 커브의 모든 좌표를 담을 배열.

    for _ in range(g): # g세대의 커브 만들기. 0123,,,,
        tmp = curve[::-1] 
        for i in range(len(tmp)):# 세대가 높아질 수록 => 이전 [curve] + [이전 curve 거꾸로 모양에 + 1]
            tmp[i] += 1
            tmp[i] %= 4 # 최대값인 3에서 +1 이되면, 다시 0. 방향은 0,1,2,3만 존재.
        
        curve = curve + tmp
    for i in curve: # curve 모양 대로, 해당하는 모든 좌표를 location 배열에 넣기.
        x,y = location[-1]
        nx = x+dx[i]
        ny = y+dy[i]
        location.append((nx,ny))
    
    
    for x,y in location: # 전체 격자판에 만들어진 커브 좌표를 표시한다.
        board[(x,y)] = 1

def countSquare(): # 정사각형 몇개인지 세기
    answer = 0
    for x,y in list(board.keys()):
        if (x,y+1) in board and (x+1,y) in board and (x+1,y+1) in board:
            answer += 1
    return answer

for _ in range(n):
    x,y,d,g = map(int,input().split())
    startCurve(x,y,d,g)
print(countSquare())
