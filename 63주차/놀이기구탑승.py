n = int(input())
g = [[0]*n for _ in range(n)]
likes = {}
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

for _ in range(n*n):
    arr = list(map(int,input().split()))
    n0 = arr[0]
    cand = []
    likes[n0] = arr[1:]
    for x in range(n):
        for y in range(n):
            if g[x][y] == 0:# 각 빈칸에 대해서, 인접 칸 중 좋아하는 사람 수, 빈칸수 세기.
                cnt,empty = 0,0
                for i in range(4):
                    nx,ny = x+dx[i],y+dy[i]
                    if inRange(nx,ny):
                        if g[nx][ny] in likes[n0]:
                            cnt += 1
                        if g[nx][ny] == 0:
                            empty += 1
                cand.append((cnt,empty,x,y))
    cand.sort(key = lambda x : (-x[0],-x[1],x[2],x[3]))# 좋아하는 사람 수 > 빈 칸 수 > 행이 작고 > 열이 작은 우선순위.
    cnt,empty, x,y = cand[0]
    g[x][y] = n0
# 점수 계산
answer = 0
for x in range(n):
    for y in range(n):
        cnt, num = 0,g[x][y]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if inRange(nx,ny) and (g[nx][ny] in likes[num]):
                cnt += 1
        if cnt > 0:
            answer += (10 ** (cnt - 1))
print(answer)
