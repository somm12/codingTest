from collections import deque
import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer =0 
circle = []
n,m,t = map(int,input().split())

for _ in range(n):
    arr = list(map(int,input().split()))
    circle.append(deque(arr))

def isRemain():
    for i in range(n):
        for j in range(m):
            if circle[i][j] !=0:
                return True
    return False

def removeOrChange():
    global circle
    flag = False# 인접하고 같은 수가 존재하는지 신호 변수.
    new = copy.deepcopy(circle)
    for x in range(n):
        for y in range(m):
            if circle[x][y] !=0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if 0 <= nx < n:
                        ny %= m # 인접한 좌표는 원판에서 1번째와 M번째도 인접하기 때문에, %m 필수.
                        if circle[x][y] == circle[nx][ny]:
                            
                            flag = True
                            new[x][y] = 0# 삭제하기.
                            new[nx][ny] = 0
    if flag:
        circle = new# 삭제한 배열로 업데이트.
    else:
        total, cnt = 0,0
        for x in range(n):
            for y in range(m):
                if circle[x][y] != 0:
                    total += circle[x][y]
                    cnt += 1
        average= total/cnt
        for x in range(n):
            for y in range(m):
                if circle[x][y] !=0:
                    if circle[x][y] > average:
                        circle[x][y] -= 1
                    elif circle[x][y] < average:
                        circle[x][y] += 1


                            
for _ in range(t):# t번 회전.
    x,d,k = map(int,input().split())
    for i in range(x-1,n,x):# x번째 원판의 배수를 d방향 k번 회전.
        if d == 0:
            for _ in range(k):
                circle[i].rotate(1)
        else:
            for _ in range(k):
                circle[i].rotate(-1)
    if isRemain():# 남아있는 수가 있으면
        removeOrChange()# 인접하고 같은 수 삭제하기 또는 평균보다 작은수 큰수 바꾸기.
    else:
        break
for i in range(n):# 총 원판에 적힌 수들의 합 구하기.
    answer += sum(circle[i])
print(answer)

    