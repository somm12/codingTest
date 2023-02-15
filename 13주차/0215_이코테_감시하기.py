from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
g = []
emp = []
teachers = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find(x,y,i):
    q= deque([(x,y)])
    while q:
        x,y = q.popleft()
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if g[nx][ny] == 'O':
                return False
            elif g[nx][ny] == 'S':
                return True
            else:
                q.append((nx,ny))
    return False
for i in range(n):
    g.append(list(input().split()))
    for j in range(n):
        if g[i][j] == 'X':
            emp.append((i,j))
        elif g[i][j] == 'T':
            teachers.append((i,j))

ans = 'NO'
for obstacle in list(combinations(emp,3)):
    detected = False
    for i,j in obstacle:
        g[i][j] = 'O'
    for a,b in teachers:
        for i in range(4):
            if find(a,b,i):
                detected = True
                break
        if detected:
            break
    if not detected:
        ans = "YES"
        break
    for i,j in obstacle:
        g[i][j] = 'X'
print(ans)
