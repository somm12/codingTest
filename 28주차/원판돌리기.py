from collections import deque
n,m,T = map(int,input().split())
circle = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    q = list(map(int,input().split()))
    circle.append(deque(q))

def rotate(i):
    global circle, d, k
    if d == 0:#시계 방향
        for _ in range(k):
            circle[i].rotate(1)
    else:# 반시계 방향.
        for _ in range(k):
            circle[i].rotate(-1)

def isExist():
    for i in range(n):
        for j in range(m):
            if circle[i][j] != -1:
                return True
    return False

def remove():
    global circle
    arr = set()
    for x in range(n):
        for y in range(m):
            if circle[x][y] != -1:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n:
                        # m == 4 일 때, 배열에서는 양끝값이지만
                        # 원에서 (0,0), (0,3) 값이 같은 경우를 위해서, (0,0),(0,-1%m)로 표현.
                        if circle[x][y] == circle[nx][ny%m]: 
                            arr.add((x,y))
                            arr.add((nx,ny%m))
    
    for x,y in arr:# 제거
        circle[x][y] = -1
    if len(arr) > 0:
        return True
    return False 

def average(): # 인접한 수가 없다면, 평균 값구해서 평균보다 큰 수는 +1, 작은 수는 -1
    global circle
    total = 0
    cnt =0
    for x in range(n):
        for y in range(m):
            if circle[x][y] != -1:
                total += circle[x][y]
                cnt += 1
    a = total/cnt

    for x in range(n):
        for y in range(m):
            if circle[x][y] != -1:
                if circle[x][y] > a:
                    circle[x][y] -=1
                elif circle[x][y] < a:
                    circle[x][y] += 1

for _ in range(T):
    x,d,k = map(int,input().split())
    for nth in range(x-1, n, x): # x-1번째(0번째 부터 시작이기에) 원판의 배수 원판을 회전시킨다.
        rotate(nth) 
    
    if isExist(): # 원판에 남아있는 수가 있다면
        if remove() == False: # 인접한 수 중에서 같은 수 제거할 것이 있다면 제거, 아니라면
            average() # 아니라면 평균값에 따라 큰 수는 -1 작은수는 +1
    else: # 남아있는 수가 없다면 총 합은 0.
        print(0)
        break
else: # 남아있는 수가 있는 거라면. 즉. T번 회전시키는 for문이 끝까지 수행되었다면,
    answer = 0
    for i in range(n):
        for j in range(m):
            if circle[i][j] != -1:
                answer += circle[i][j]
    print(answer)
# 원판에 적힌 수 합. 구하기