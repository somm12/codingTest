from collections import deque
n = int(input())
g = [[0]*n for _ in range(n)]
a = int(input())
for _ in range(a):
    x,y = map(int,input().split())
    g[x-1][y-1] = 1


rotate= deque()
L = int(input())
for _ in range(L):
    t,di = input().split()
    rotate.append((int(t),di))
d = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

time =0
snake = deque()
snake.append((0,0))
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def move():
    global g, snake
    x,y = snake[-1]
    nx,ny = x+dx[d],y+dy[d]
    if not inRange(nx,ny):# 범위 벗어남.
        return False
    if (nx,ny) in snake:# 자기 몸과 부딪힘.
        return False
    snake.append((nx,ny))
    return True

def isApple():
    global g, snake
    x,y = snake[-1]# 마지막 원소가 머리.
    if g[x][y] == 1:
        g[x][y] = 0
    else:# 사과 없다면 꼬리였는 부분 pop
        snake.popleft()


while True:
    
    if not move():
        print(time+1)
        break
    isApple()
    time += 1
   
    if rotate and rotate[0][0] ==time:# 회전할 타임.
        _,di = rotate.popleft()
        if di == 'D':
            d = (d+1)%4
        else:
            d = (d-1)%4

#백준 뱀.