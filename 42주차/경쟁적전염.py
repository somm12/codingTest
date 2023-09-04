n, k =map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

s,x,y = map(int,input().split())
x -= 1
y -= 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = []

for i in range(n):
    for j in range(n):
        if g[i][j] !=0:
            q.append((g[i][j],i,j,0))
q.sort()# 낮은 번호 부터 처리 => sort.

while q:
    num,i,j,t = q.pop(0)
    if t >= s:# s초까지 지났다면, break
        break
    for d in range(4):
        nx = i+dx[d]
        ny = j+dy[d]
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:# 빈칸일 경우에만 퍼짐.
            g[nx][ny] = num
            q.append((num,nx,ny,t+1))
print(g[x][y])
