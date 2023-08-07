import copy
n,m = map(int,input().split())
answer = 64
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cctv = [[],[[0],[1],[2],[3] ], [[2,3], [0,1]], [ [0,2],[0,3], [1,2],[1,3]],
[[0,1,2],[0,1,3],[0,2,3],[1,2,3]],[ [0,1,2,3] ] ]

g = []
cctvList = []
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if 1 <= g[i][j] <=5:
            cctvList.append((i,j))

def spread(arr):
    tmp= copy.deepcopy(g)
    for i,v in enumerate(cctvList):
        x,y = v
        for d in arr[i]:
            nx,ny=x,y
            while True:
                nx += dx[d]
                ny += dy[d]
        
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp[nx][ny] == 0:
                        tmp[nx][ny] = -1
                    elif tmp[nx][ny] == 6:
                        
                        break
                else:
                    
                    break
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(L,res):
    global answer
    if L ==len(cctvList):
    
        answer = min(spread(res),answer)
        return
    
    x,y = cctvList[L]
    num = g[x][y]
    for arr in cctv[num]:
        res.append(arr)
        dfs(L+1, res)
        res.pop()



dfs(0,[])
print(answer)