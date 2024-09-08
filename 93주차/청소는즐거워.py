n = int(input())
g =[]
for _ in range(n):
    g.append(list(map(int,input().split())))
def inRange(x,y):
    return 0 <= x < n and 0<= y < n

answer  =0
dx = [0, 1,0,-1]
dy = [-1,0,1,0]

spread = [[(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),(-1,1,0.01),(1,1,0.01),(0,-2,0.05)],
          [(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(-1,-1,0.01),(-1,1,0.01),(1,-1,0.1),(1,1,0.1),(2,0,0.05)],
          [(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),(-1,1,0.1),(1,1,0.1),(0,2,0.05)],
          [(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),(-1,-1,0.1),(-1,1,0.1),(1,-1,0.01),(1,1,0.01),(-2,0,0.05)]]


x,y= n//2,n//2
d = 0
cnt =0
while True:
    if not inRange(x,y): break# 0,0 좌표를 넘어섬. 끝!
    if d % 2 ==0:
        cnt += 1
    for _ in range(cnt):
        x += dx[d]
        y += dy[d]
        if inRange(x,y):
            total = 0
            for i,j,v in spread[d]:

                tx,ty = x+i,y+j
                tv = int(g[x][y]*v)
                total += tv
                if inRange(tx,ty):
                    g[tx][ty] += tv

                else:# 격자 밖으로 나가는 먼지양.
                    answer += tv

            tx,ty = x+dx[d],y+dy[d]
            if inRange(tx,ty):# a% 로 가는 남은 먼지양
                g[tx][ty] += (g[x][y]-total)
            else:# 격자 밖으로 가는 먼지양 
                answer += (g[x][y]-total)

            g[x][y] = 0# 빗자루 부분은 0이 됨.
    

    d = (d+1)%4

print(answer)
# 코드트리 청소는즐거워