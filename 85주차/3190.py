n = int(input())
cnt = int(input())
g = [[0]*n for _ in range(n)]
for _ in range(cnt):
    x,y = map(int,input().split())
    g[x-1][y-1] =1

k = int(input())
arr = []
for _ in range(k):
    time,d = input().split()
    arr.append((int(time),d))
arr = arr[::-1]
idx =0
snake = [(0,0)]
t = 0# 몇 초에 게임이 끝나는지 저장할 현재 시간. 

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def inRange(x,y):
    return 0 <=x < n and 0 <= y <n
def move():
    global snake

    hx,hy = snake[0]
    nx,ny = hx+dx[idx],hy +dy[idx]
    if not inRange(nx,ny) or (nx,ny) in snake:
        return False
    snake= [(nx,ny)] + snake
    if g[nx][ny] == 1:
        g[nx][ny] = 0
    else:
        snake.pop()
    return True


while True:
    if move():# 이동 
        t+=1
        if arr and arr[-1][0] == t:# 방향 전환할 시점이라면,
            if arr[-1][1] == 'D':# 오른쪽으로 방향 전환
                idx = (idx+1)%4
            else:# 왼쪽으로 방향 전환.
                idx = (idx-1)%4
            arr.pop()
    
    else:
        print(t+1)
        break

# 백준 뱀
