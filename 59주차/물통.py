from collections import deque
A,B,C = map(int,input().split())
visited = [[0]*(C+1) for _ in range(A+1)]
q = deque()
x,y,z = 0,0,C
q.append((x,y,z))
visited[x][z] = 1
answer = []
while q:
    x,y,z = q.popleft()
    
    if x == 0:
        answer.append(z)
    if x > 0:
        # x->y
        if B - y >= x:# x가 빌때 까지
            nx,ny,nz= 0,y+x,z
        else:
            nx,ny,nz = x - (B-y),B,z
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
        # x - > z:
        if C - z >= x:
            nx,ny,nz = 0,y,z+x
        else:
            nx,ny,nz = x - (C-z), y, C
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
    if y > 0:
        # y->x
        if A - x >= y:
            nx,ny,nz= x+y, 0,z
        else:
            nx,ny,nz= A, y - (A-x),z
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
        # y->z
        if C - z >= y:
            nx,ny,nz = x,0,z+y
        else:
            nx,ny,nz = x, y - (C-z), C
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
    if z > 0:
        # z-> x
        if A - x >= z:
            nx,ny,nz= x+z, y,0
        else:
            nx,ny,nz= A, y,z - (A - x)
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
        # z -> y
        if B - y >= z:
            nx,ny,nz= x,y+z,0
        else:
            nx,ny,nz = x,B,z - (B-y)
        if not visited[nx][nz]:
            visited[nx][nz]=1
            q.append((nx,ny,nz))
answer.sort()
for v in answer:
    print(v,end=' ')
