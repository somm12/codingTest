n = int(input())
target = int(input())
dx = [-1,0,1,0]
dy= [0,1,0,-1]
K = n//2
g = [[0]*n for _ in range(n)]
x,y = K,K

cnt = 0
g[x][y] = 1
num = 2
d = 0
tx,ty= x,y # 찾을려고하는 숫자의 위치

while 0 <= x < n and 0 <= y < n: # 상 우 하(2번) 좌(2번) | 상(3번) 우(3번) 하(4번) 좌(4번),,
    if d % 2 == 0:
        cnt += 1
    for _ in range(cnt):
        x += dx[d]
        y += dy[d]
        if 0 <= x < n and 0 <= y < n:
            g[x][y] = num
            num += 1
        else:
            break
    d = (d+1)%4

for x in range(n):
    for y in range(n):
        print(g[x][y],end=' ')
        if g[x][y] == target:
            tx,ty = x+1,y+1
    print()

print(tx,ty)
# 달팽이 문제