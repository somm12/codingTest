n,m = map(int,input().split())
g = []
dx = [-1,1,0,0]
dy= [0,0,-1,1]
cctv = []# cctv 위치
# cctv 각 번호별로 가질 수 있는 방향 경우의 수.
cctvType = [[],[[0],[1],[2],[3]], [[0,1],[2,3]],[[0,2],[0,3],[1,2],[1,3]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[[0,1,2,3]]]
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if 1 <= g[i][j] <= 5:
            cctv.append((i,j))

answer =64 # 최대 넓이는 8*8

def inRange(x,y):
    return 0 <=x < n and 0 <= y < m

def getArea(tmp):# 사각 지대 구하기.
    cnt = 0
    for x in range(n):
        for y in range(m):
            if tmp[x][y] == 0:
                cnt += 1
    return cnt 


def watch(arr):# 각 cctv에게 할당 된 방향이 결정된 arr를 가지고 감시하기
    tmp = [a[:] for a in g]
    for i in range(len(cctv)):
        x,y =cctv[i]
        for d in arr[i]:
            nx,ny=x,y
            while True:
                nx += dx[d]
                ny += dy[d]
                if not inRange(nx,ny) or g[nx][ny] == 6: break# 벽 만나면 그만 
                elif g[nx][ny] == 0:# 0 만나면 감시 해당. 1~5 등 다른 cctv는 통과 가능.
                    tmp[nx][ny] = '#'
    return tmp


def dfs(L,res):# L 번째 cctv의 방향 정하기. res는 L번째 카메라가 가지는 방향을 저장.
    global answer
    if L == len(cctv):
        
        tmp= watch(res)# 감시 시작.
        answer = min(answer,getArea(tmp))# 사각지대 구하기. 
        return
    x,y = cctv[L]
    num = g[x][y]
    for arr in cctvType[num]:
        res.append(arr)
        dfs(L+1,res)
        res.pop()
        
dfs(0,[])
print(answer)
# 백준 감시