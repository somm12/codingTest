from collections import deque

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer =0

def findGroup():# 상하좌우 인접하며 같은 색깔을 가진 그룹 찾기.
    team = []
    visited = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                tmp = []
                value =g[x][y]
                visited[x][y] = 1
                q= deque()
                q.append((x,y))
                while q:
                    a,b = q.popleft()
                    tmp.append((a,b))
                    for i in range(4):
                        nx = a+dx[i]
                        ny = b+dy[i]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == value:
                            visited[nx][ny] =1
                            q.append((nx,ny))
                team.append(tmp)
    return team

def combi(num):# 조합 구하기.
    total =[]
    def comb(start,res):
        if len(res)==2:
            total.append(res)
            return
        for i in range(start,num):
            comb(i+1,res+[i])
    comb(0,[])
    return total

def calcScore(arr1,arr2):# arr1,arr2의 예술점수 계산
    length1 = len(arr1)
    length2 = len(arr2)

    x,y =arr1[0]
    num1 = g[x][y]

    x,y = arr2[0]
    num2 = g[x][y]
    cnt = 0

    for x,y in arr1:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx,ny) in arr2:
                cnt += 1
    return (length1+length2) * (num1)*(num2)*cnt

def rotate():# 십자가 부분은 반시계 90 도 회전. 나머지 정사각형 4개 부분은 시계방향 회전.
    global g
    tmp = [[0]*n for _ in range(n)]
    after = [[0]*n for _ in range(n)]# 최종 회전 결과 담을 배열.

    for i in range(n):# 십자가 부분만 따로 담기
        tmp[i][n//2] = g[i][n//2]
        tmp[n//2][i] = g[n//2][i]

    for x in range(n):# 십자가는 반시계 90 회전
        for y in range(n):
            after[n-1-y][x] = tmp[x][y]

    L = n//2
    arr = [(0,0),(0,L+1), (L+1,0),(L+1,L+1)]
    for i,j in arr:# 나머지 4개 정사각형 시계 90 회전
        for x in range(L):
            for y in range(L):
                after[y + i][L -1 -x +j] = g[x + i][y + j]
    g = after


def getScore():
    global answer

    group = findGroup()# 그룹 찾기
    arr = combi(len(group))# 그룹 조합 (2쌍) 구하기

    for a,b in arr:
        point = calcScore(group[a],group[b])# 그룹 a,b끼리 예술 점수 구하기.
        answer += point

getScore() # 초기 점수 구하기.
for m in range(1,4):
    rotate()
    getScore()

print(answer)