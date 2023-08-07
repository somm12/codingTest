from collections import deque
import copy
circle = []
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,T = map(int,input().split())
for _ in range(n):
    a = list(map(int,input().split()))
    circle.append(deque(a))

def rotate():# 회전하기.
    global x,d,k,circle
    for i in range(x-1,n,x):
        if d == 0:
            for _ in range(k):
                circle[i].rotate(1)
        else:
            for _ in range(k):
                circle[i].rotate(-1)

def isRemain():# 남은 숫자가 있는지 확인.
    global circle
    for arr in circle:
        for v in arr:
            if v >0 :
                return True
    return False

def remove():# 인접하면서 같은 숫자는 제거하기. 그러한 숫자가 있다면 True반환. 없는 수는 0으로 표현해서 0은 제외하는 것에 유의.
    global circle
    tmp = copy.deepcopy(circle)
    flag =False

    for x in range(n):
        for y in range(m):
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx <n:
                    ny %= m
                    if circle[nx][ny] == circle[x][y] and circle[x][y] != 0:
                        flag = True
                        tmp[nx][ny] = 0
                        tmp[x][y] =0
    circle = tmp
    return flag
def average():# 평균을 구하고, 원판 번호 숫자 변경.
    global circle
    total = 0
    cnt =0
    for i in range(n):
        for j in range(m):
            if circle[i][j] >0 :
                total +=circle[i][j]
                cnt += 1
    aver = (total/cnt)
    for i in range(n):
        for j in range(m):
            if circle[i][j] > 0:
                if circle[i][j] > aver:
                    circle[i][j] -= 1
                elif circle[i][j] < aver:
                    circle[i][j] += 1

for _ in range(T):
    x,d,k =map(int,input().split())
    rotate() # x번 배수 원판을 d방향으로 k칸 회전.
    if isRemain(): # 원판에 수가 남았다면
        if remove(): # 인접하면서 값이 같은 숫자가 있다면 제거
            continue
        else: # 그런 숫자가 없다면 평균을 구해서 평균보다 작으면 +1, 크면 -1.
            average()

for arr in circle:# 남은 원판 숫자들의 합.
    answer += sum(arr)
print(answer)