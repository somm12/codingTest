n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
answer =0
dx= [0,1,0,-1]
dy=[ -1,0,1,0]#좌 하 우 상
sx,sy = n//2,n//2# 정 가운데 좌표.

flag = True
cnt, d = 0,0
# 좌 하 우 상 순서대로 비율.
rate = [[(-1,0,0.07), (1,0,0.07),(-1,-1,0.1), (1,-1,0.1), (-1,1,0.01),(1,1,0.01), (-2,0,0.02),
         (2,0,0.02),(0,-2,0.05)],

        [(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(1,-1,0.1),(1,1,0.1),(0,-2,0.02),
         (0,2,0.02), (2,0,0.05)],
        [(-1,-1,0.01), (1,-1,0.01), (-1,1,0.1), (1,1,0.1), (-1,0,0.07), (1,0,0.07), (-2,0,0.02),
         (2,0,0.02), (0,2,0.05)],
        [(-1,-1,0.1), (-1,1,0.1), (0,-1,0.07), (0,1,0.07),(1,-1,0.01),(1,1,0.01), (0,-2,0.02),
         (0,2,0.02), (-2,0,0.05)]]
while flag:
    if d %2 == 0:
        cnt += 1
    for _ in range(cnt):
        sx += dx[d]
        sy += dy[d]
        now = g[sx][sy]
        remain = now
        # 각 비율로 퍼지기.
        for x,y,r in rate[d]:
            nx = sx+x
            ny = sy+y
            value = int(now*r)
            remain -= value
            if 0 <= nx < n and 0 <= ny <n :
                g[nx][ny] += value
            else:# 벗어나면 answer에 추가.
                answer += value
        # 남은 먼지양은 알파 영역에 추가.
        nx = sx+dx[d]
        ny = sy+dy[d]
        if 0 <= nx < n and 0 <= ny <n:
            g[nx][ny] += remain
        else:# 알파 영역도 격자 밖이면 answer에 추가.
            answer += remain
        # 이동한 자리는 0이 됨
        g[sx][sy] = 0

      
        if sx == 0 and sy == 0:# 0,0에 도달하면 종료.
            flag = False
            break


    d= (d+1)%4
print(answer)
# 삼성 기출 코드트리.