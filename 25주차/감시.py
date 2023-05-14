n, m = map(int,input().split())
# 각 cctv가 종류에 따라 갈 수 있는 방향을 나타낸 배열 (0,1,2,3 : 상 하 좌 우)
direction = [[],[[0],[1],[2],[3]],[[0,1],[2,3]], [[0,3],[1,3],[1,2],[0,2]],[[0,1,2],[0,1,3],[0,2,3],[1,2,3]], [[0,1,2,3]]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
g = []
# cctv위치를 담을 배열.
cctv = []
answer = int(1e9)
for i in range(n):
    g.append(list(map(int,input().split()))) 
    for j in range(m):
        if 1 <= g[i][j] <= 5: # cctv 위치 담기
            cctv.append((i,j))
# 감시하는 함수: 각 cctv들이 바라볼 수 있는 모든 방향 조합 구하기.(중복 가능 ex 2번 cctv 모두 같은 방향)
def see(arr,new):
    for i, v in enumerate(arr): # cctv들의 방향정보가 든 arr.
        for d in v:
            rx = cctv[i][0] # 현재 i번째 cctv의 x,y 좌표.
            ry = cctv[i][1]
            while True:# 감시 가능한 모든 방향에 대해서 -1 할당.
                rx += dx[d]
                ry += dy[d]
                if 0 <= rx < n and 0 <= ry < m: # 범위를 벗어나면 break
                    if g[rx][ry] == 6: # 벽을 만나면 통과 못함.
                        break
                    if 1 <= g[rx][ry] <=5 : # 다른 cctv는 통과 가능.
                        continue
                    if g[rx][ry] == 0:
                        new[rx][ry] = -1
                else:
                    break
# 최소 사각 사각지대 구하기. 즉, 0의 개수를 구하고 최소 사각지대 크기 업데이트하는 함수
def area(new):
    global answer
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new[i][j]==0:
                cnt += 1
    answer = min(cnt,answer)

# cctv들의 위치를 담은 배열 cctv의 idex를 이용해서(L) 갈 수 있는 방향들 중 하나를 뽑고
# 이어서 다음 idx로 넘어가서 해당 cctv가 갈 수 있는 방향을 정하는 방식 -> 중복 가능.
def dfs(L,res):
    if L == len(cctv): # 모든 cctv들의 감시 방향을 정하고 난 후 하나의 경우가 되었을 때.
        # 감시할 때 사무실 2차원 배열 값을 바꿀 때 사용할 new 배열에 g 복사.
        new = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new[i][j] = g[i][j]
        # 감시 후, 사각지대 크기 구하기.
        see(res,new)
        area(new)
        return
    # 현재 L 인덱스에 해당하는 cctv의 행과 열의 위치.
    x = cctv[L][0] 
    y = cctv[L][1]
    # 현재 cctv가 갈 수 있는 모든 방향 중 하나를 골라서 res 배열에 append
    # res => [[1번 cctv 방향],[2번 cctv 방향],,,,,,]
    for d in direction[g[x][y]]:
        res.append(d)
        dfs(L+1,res)
        res.pop()
    
dfs(0,[])
print(answer)