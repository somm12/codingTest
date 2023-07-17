from collections import deque
import copy
n,m,T = map(int,input().split())
circle = [[]]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    q = list(map(int,input().split()))
    circle.append(deque(q))

def check(x):
    global circle
    flag = False
    
    for y in range(m):
        tmp = circle[x][y]
        if tmp != 0:
            for i in range(4):
                nx = x+dx[i]
                ny = y + dy[i]
                if 1 <= nx <= n and 0 <= ny < m:
                    if circle[nx][ny] == tmp:
                        # print(x,y,nx,ny, circle[nx][ny])
                        # circle[nx][ny] = 0
                        # circle[x][y] = 0
                        flag = True
    return flag
def erase():
    global circle
    tmp = copy.deepcopy(circle)
    
    for x in range(1,n+1):
        for y in range(m):
            if circle[x][y] != 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = (y + dy[i])%m

                    if 1 <= nx <= n:
                        if circle[nx][ny] == circle[x][y]:
                            tmp[nx][ny] = 0
                            tmp[x][y] = 0
                            
    circle = tmp
    
def change():
    # 인접하고 수가 같은 수가 없다면.
    total = 0
    count = 0
    for x in range(1,n+1):
        total += sum(circle[x])
        for y in range(m):
            if circle[x][y] != 0:
                count += 1
    if total == 0:
        return
    average = total/count
    for x in range(1,n+1):
        for y in range(m):
            if circle[x][y] != 0:
                if circle[x][y] > average:
                    circle[x][y] -= 1
                elif circle[x][y] < average:
                    circle[x][y] += 1


for _ in range(T):
    x,d,k = map(int,input().split()) #x배수 번째 원판을 d방향으로 k번 회전.
    for i in range(x, n+1,x):
        if d == 0:#시계
            for _ in range(k):
                circle[i].rotate(1)
        else:
            for _ in range(k):
                circle[i].rotate(-1)
    cnt = 0
    for i in range(1,n+1):# 모든 원판에 대해서 인접하고 같은 수 있는지 확인.
        if not check(i):
            cnt += 1
    if cnt == n:
        change()
    else:
        erase()


for arr in circle:
    
    answer += sum(arr)
print(answer)

# 숫자가 남아있다면, 조건
# 인접한 수를 찾을 때, column에서 1번과 N, 1번과 2번 이 인접하는 부분.