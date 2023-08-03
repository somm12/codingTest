n = int(input())
g = []
import math
answer = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]
for _ in range(n):
    g.append(list(map(int,input().split())))
sx,sy = n//2, n//2

cnt = 0
d = 0
rate = [ [[0,-2,0.05],[-1,-1,0.1],[-1,0,0.07],[-2,0,0.02],[-1,1,0.01],
[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02] ] ,[
    [-1,-1,0.01],[-1,1,0.01],[0,-1,0.07],[0,1,0.07],[1,-1,0.1],[1,1,0.1],[0,-2,0.02],
    [0,2,0.02],[2,0,0.05]
], [ [-1,-1,0.01],[1,-1,0.01],[-1,0,0.07],[1,0,0.07],[-2,0,0.02],[2,0,0.02],[-1,1,0.1],
[0,2,0.05],[1,1,0.1]
]

 ,[[1,-1,0.01],[1,1,0.01],[0,-1,0.07],[0,1,0.07],[0,-2,0.02],[0,2,0.02],[-1,-1,0.1],
 [-1,1,0.1],[-2,0,0.05]]  ]

while True:
    if not (0 <= sx < n and 0 <= sy < n):
        break
    if d % 2 == 0:
        cnt += 1
    
    for _ in range(cnt):
        sx += dx[d]
        sy += dy[d]
        total = g[sx][sy]
        remain = total

        for x,y,r in rate[d]:
          
            nx = sx+x
            ny = sy+y
            remain -= math.floor(total*r)
            if 0 <= nx < n and 0 <= ny < n:
                g[nx][ny] += math.floor(total*r)
            else:
                answer += math.floor(total*r)
        nx = sx+dx[d]
        ny = sy+dy[d]
        if 0 <= nx < n and 0<= ny <n:
            g[nx][ny] += remain
        else:
            answer += remain
        g[sx][sy]=0
       
       
    d += 1
    d %= 4
        
print(answer)