import sys
input = sys.stdin.readline
n,k = map(int,input().split())

g= [ ]
dx= [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    g.append(list(map(int,input().split())))
s,X,Y = map(int,input().split())
X -=1
Y -=1
q = []
for i in range(n):# 큐에 바이러스 번호 다 넣기
    for j in range(n):
        if g[i][j] != 0:
            q.append((g[i][j],i,j,0))
q.sort()# 낮은 번호 순이므로, 정렬.
while q:# 차례로 바이러스가 퍼지며, s초가 지난 순간 break
    num,x,y,t = q.pop(0)
    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:
            g[nx][ny] = num
            q.append((num,nx,ny,t+1))
print(g[X][Y])# 해당 좌표의 바이러스 번호 