n = int(input())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer =0 

def dfs(x,y,visited, value,res):# 같은 숫자를 가진 각 그룹을 만들기. res에 모든 좌표를 추가.

    
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and g[nx][ny] == value:
            res.append((nx,ny))
            dfs(nx,ny,visited,value,res)
    return res
# def dfs(x,y,visited, value,res):
  
   
#     visited[x][y] = 1
#     stack = [(x,y)]
#     while stack:
#         x, y = stack.pop()
#         for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#             nx, ny = x + di, y + dj
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and value == g[nx][ny]:
#                 visited[nx][ny] = 1
#                 stack.append((nx, ny))
#                 res.append((nx,ny))
                
#     return res
def combi(length):# 2쌍씩 조합 구하기.
    arr = []
    def com(res,start):
        if len(res) == 2:
            arr.append(res)
            return
        for i in range(start,length):
            com(res+[i],i+1)
    com([],0)

    return arr

def rotate():# 회전하기.
    global g
    newG = [[0]*n for _ in range(n)]
    # 십자 모양은 반시계 90도 회전
    # col
    for i in range(n):
        newG[n//2][i] = g[i][n//2]
    #row
    for j in range(n):
        newG[n-1-j][n//2] = g[n//2][j]
    # 나머지 정사각형 4부분은 시계방향 90도 회전.
    mid = n//2
    coord = [(0,0), (0,mid+1), (mid+1, 0), (mid + 1,mid+1)]
    for i,j in coord:
        for x in range(mid):
            for y in range(mid):
                newG[y+i][(mid-1-x)+j] = g[x+i][y+j]
    g = newG

def countingLine(arr,arr2):# 그룹 두 개 사이의 맞닿은 변의 개수를 구하기.
    cnt  = 0
    for x,y in arr:
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (nx,ny) in arr2:
                    cnt += 1
    return cnt
def makeG():
    visited = [[0]*n for _ in range(n)]
    arr = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                arr.append(dfs(i,j,visited,g[i][j],[(i,j)]))
    return arr

def getPoint():
    global answer
    group = makeG()# 그룹만들기
    comb = combi(len(group))# 조합 구하기. (인덱스를 이용해서 2쌍 조합을 만들기)
    for i1,i2 in comb:
        harmony = len(group[i1]) + len(group[i2])# 각 칸 개수.
        x1,y1 = group[i1][0]
        x2,y2 = group[i2][0]
        v1 = g[x1][y1]# 해당 그룹의 색 점수 구하기.
        v2 = g[x2][y2]

        harmony *= (v1*v2)
        harmony *= (countingLine(group[i1],group[i2]))# 서로 맞닿은 변의 개수 구하기.
        answer += harmony


getPoint()# 초기 점수
for i in range(3): # 회전 이후, 3회차 회전 이후 점수까지 구하기.
    rotate()
    getPoint()
print(answer)
# 변이 맞닿아 있는 개수 부분.
# 부분 회전 .