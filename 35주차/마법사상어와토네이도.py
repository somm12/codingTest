g = []
n = int(input())
dx = [0,1,0,-1]
dy = [-1,0,1,0]
for _ in range(n):
    g.append(list(map(int,input().split())))
# 좌 하 우 상
arr = [[(-1,0,7),(1,0,7),(-1,-1,10),(1,-1,10),(-1,1,1),(1,1,1),(-2,0,2),(2,0,2),(0,-2,5)],
[(-1,-1,1),(-1,1,1),(0,-1,7),(0,1,7),(1,-1,10),(1,1,10),(0,-2,2), (0,2,2),(2,0,5)],
[(-1,0,7),(1,0,7),(-1,1,10),(1,1,10),(-1,-1,1),(1,-1,1),(-2,0,2),(2,0,2),(0,2,5)],
[(-1,-1,10),(-1,1,10),(0,-1,7),(0,1,7),(1,-1,1),(1,1,1),(-2,0,5),(0,-2,2),(0,2,2)]]

answer = 0
def spread(x,y,d):# x,y 지점에서 d방향으로 움직일 때, 모래가 흩날리는 함수.
    global g,answer
    sand = g[x][y]

    remain = g[x][y]
    for i,j,v in arr[d]:
        nx = x+i
        ny = y+j
        
        temp = int(sand* (v/100))
        if 0 <= nx < n and 0<= ny <n:
            g[nx][ny] += temp
            remain -= temp
        else:
            answer += temp
            remain -= temp
    nx = x+dx[d]
    ny = y + dy[d]
    if 0<= nx < n and 0 <= ny < n:
        g[nx][ny] += remain
    else:
        answer += remain
    g[x][y] = 0
    
 
def go():
    d = 0
    cnt = 0
    x,y = n//2,n//2

    while True:
        if d % 2 == 0:
            cnt += 1
        for _ in range(cnt):
            x += dx[d]
            y += dy[d]
            # 문제 설명에서 x -> y방향 일때 y기준 주변 모래 흩날리는 비율로 모래가 퍼진다.
            if x <0 or y <0:
                return 
            spread(x,y,d)
        d += 1
        d %= 4
        
    

go() 
print(answer)