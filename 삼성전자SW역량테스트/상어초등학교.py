n = int(input())
dict = {}
for _ in range(n**2):
    nth,a,b,c,d = map(int,input().split())
    dict[nth] = [a,b,c,d]
g = [[0]*n for _ in range(n)]

dx =[-1,1,0,0]
dy = [0,0,-1,1]
for k in list(dict.keys()):
    seat = []
    for x in range(n):
        for y in range(n):
            if g[x][y] == 0:
                like = 0
                empty = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0<=ny < n:
                        if g[nx][ny] in dict[k]:
                            like += 1
                        elif g[nx][ny] == 0:
                            empty += 1
                seat.append((like,empty,x,y))
    seat.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    i,j = seat[0][2], seat[0][3]
    g[i][j] = k
a = [0,1,10,100,1000]
answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny <n:
                if g[nx][ny] in dict[g[x][y]]:
                    cnt += 1
        answer += a[cnt]
print(answer)