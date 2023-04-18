from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def lever(maps,s):
    n = len(maps)
    m = len(maps[0])
    x,y = s[0],s[1]
    check = [[0]*m for _ in range(n)]
    q = deque()
    check[x][y] = 1
    q.append((x,y,0))
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and not check[nx][ny]:
                if maps[nx][ny] != 'X':
                    check[nx][ny] = 1
                    if maps[nx][ny] == 'L':
                        return dist + 1
                    q.append((nx,ny,dist+1))
    return -1

def door(maps,l):
    n = len(maps)
    m = len(maps[0])
    x,y = l[0],l[1]
    check = [[0]*m for _ in range(n)]
    q = deque()
    check[x][y] = 1
    q.append((x,y,0))
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny <m and not check[nx][ny]:
                if maps[nx][ny] != 'X':
                    check[nx][ny] = 1
                    if maps[nx][ny] == 'E':
                        return dist + 1
                    q.append((nx,ny,dist+1))
    return -1

def solution(maps):
    answer = 0
    s = []
    l = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = [i,j]
            elif maps[i][j] == 'L':
                l = [i,j]
          
    d1 = lever(maps,s)
    if d1 == -1:
        return -1
    answer += d1
    
    d2 = door(maps,l)
    if d2 == -1:
        return -1
    answer += d2
    return answer
