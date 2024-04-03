arr = [[(-2,0,0.02), (-1,-1,0.1), (-1,0,0.07),(-1,1,0.01), (0,-2,0.05),(1,-1,0.1),(1,0,0.07), (1,1,0.01),(2,0,0.02)]
,[(-1,-1,0.01),(-1,1,0.01),(0,-2,0.02),(0,2,0.02),(0,-1,0.07),(0,1,0.07),(1,-1,0.1),(1,1,0.1),(2,0,0.05)]
,[(-1,-1,0.01),(1,-1,0.01),(-2,0,0.02),(2,0,0.02),(-1,0,0.07),(1,0,0.07),(-1,1,0.1),(1,1,0.1),(0,2,0.05)]
,[(1,-1,0.01),(1,1,0.01),(0,-2,0.02),(0,2,0.02),(0,-1,0.07),(0,1,0.07),(-1,-1,0.1),(-1,1,0.1),(-2,0,0.05)]
]
# 각 좌 하 우 상 방향일 때, 먼지가 더해질 위치에 맞는 비율을 담은 배열.
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer = 0
dx =[0,1,0,-1]
dy = [-1,0,1,0]

lx,ly = n//2,n//2# 빗자루 위치.
d = 0
cnt = 0
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

while inRange(lx,ly):
    if d % 2 == 0:
        cnt += 1
    for _ in range(cnt):
        lx += dx[d]
        ly += dy[d]
        
        if inRange(lx,ly):
            target = g[lx][ly]
            total = 0
            for a,b, rate in arr[d]:# 현재 빗자루 위치로 부터 퍼질 먼지 계산.
                nx = lx+a
                ny = ly+b
                value = int(target*rate)
                total += value# 각 비율에 해당 하는 먼지 더하기.
                if inRange(nx,ny):
                    g[nx][ny] += value
                else:# 격자 밖으로 나간 먼지 계산
                    answer += value
            nx = lx + dx[d] # a%. 남은 비율 처리.
            ny = ly + dy[d]
            if inRange(nx,ny):
                g[nx][ny] += (target - total)
            else:# 격자 밖으로 나간 먼지 계산
                answer += (target - total)
            g[lx][ly] = 0# cur로 움직인 먼지 자리는 먼지가 사라짐.
           
    d = (d+1)%4

print(answer)