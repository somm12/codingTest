dx = [0,1,0,-1]
dy = [-1,0,1,0]
# 좌 하 우 상 순서로, 위치와 비율 지정.
dust = [[(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),(-1,1,0.01),(1,1,0.01),(0,-2,0.05)],
[(0,-1,0.07),(0,1,0.07),(-1,-1,0.01),(-1,1,0.01),(0,-2,0.02),(0,2,0.02),(1,-1,0.1),(1,1,0.1),(2,0,0.05)],
[(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.1),(1,1,0.1),(-1,-1,0.01),(1,-1,0.01),(0,2,0.05)],
[(-1,-1,0.1),(-1,1,0.1),(0,-1,0.07),(0,1,0.07),(-2,0,0.05),(0,-2,0.02),(0,2,0.02),(1,-1,0.01),(1,1,0.01)]
]

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

answer = 0
sx,sy = n//2,n//2

cnt = 0
d = 0
def inRange(x,y):
    return 0 <= x< n and 0 <= y < n
while True:
    if not inRange(sx,sy):
        break
    if d%2 == 0:
        cnt += 1
   
    for _ in range(cnt):
        sx += dx[d]
        sy += dy[d]
        if not inRange(sx,sy):
            break
        num = g[sx][sy]
        remain = num
        for i,j,p in dust[d]:
            nx,ny = sx+i, sy+j
            add =int(num*p)
            if inRange(nx,ny):
                g[nx][ny] += add
            else:
                answer += add #격자 밖으로 이동일 때
            remain -= add
        nx,ny = sx+dx[d],sy+dy[d]
        if inRange(nx,ny):# 먼지가 다른 격자로 이동하고 남은 양이 더해짐.
            g[nx][ny] += remain
        else:
            answer += remain #격자 밖으로 이동일 때
        g[sx][sy] = 0
    d =(d+1)%4

print(answer)
