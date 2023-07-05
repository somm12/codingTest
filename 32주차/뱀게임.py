n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
direction = 0
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
q= []
for _ in range(L):
    a,b = input().split()
    q.append((int(a),b))
now = 0
snake= [(0,0)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move():
    global board,now,snake
    now += 1 # 시간 증가
    x,y = snake[-1]# 배열의 가장 끝 부분 즉, 머리 좌표 꺼내기
    nx = dx[direction] + x
    ny = dy[direction] + y
    if not (0 <= nx < n and 0 <= ny < n): # 벽을 만나면 false
        return False
    if (nx,ny) in snake:# 자기 몸과 부딪히면 false
        return False
    snake.append((nx,ny))# 머리 갱신

    if board[nx][ny] == 1: # 이동 칸에 사과가 있으면 사과 없애기. 길이는 +1이 됨
        board[nx][ny]= 0
    else:
        snake.pop(0) # 사과가 없으면, 꼬리 자르기, 길이는 그대로.
    return True


while True: # 뱀이 벽을 만나거나, 자기 몸과 부딪힐 때까지 움직인다.
    if q:
        t,d = q[0] # 최근 방향 바뀌는 정보 확인. 시간, 방향 반환.
    if t == now: # 현재 시간이 방향이 바뀌는 시점일때, 방향 전환
        q.pop(0)
        if d == 'L': # 왼쪽 일 경우
            direction = (direction-1)%4
        else:# 오른쪽일 경우
            direction = (direction+1)%4
    if not move():# 현재 바라보는 쪽으로 움직이기.
        break


print(now)# 게임이 끝난시점 반환. 이동 때마다 초가 증가한다고 보면 됨.
