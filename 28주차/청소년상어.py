dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

fish = [[0]*3 for _ in range(17)]
g = []
answer = 0
for i in range(4):
    a = list(map(int,input().split()))
    g.append([a[0],a[2],a[4],a[6]])
    for j in range(4):
        fish[g[i][j]] = [i,j, a[j*2 + 1]-1]

shark = [0,0,fish[g[0][0]][2]]
answer += g[0][0]
fish[g[0][0]] = [-1,-1,-1]
g[0][0] = -1

print(fish)

def fishM():
    global g,fish
    for i,v in enumerate(fish):
        if sum(v) >= 0:
            x,y,d = v
            nx = x
            ny = y
            idx = d
            for _ in range(8):
                nx += dx[idx]
                ny += dy[idx]
                idx += 1
                idx %= 8
                
                if 0 <= nx < 4 and 0 <= ny < 4 and [shark[0],shark[1]] != [nx,ny]:
                    f = g[x][y]
                    t = g[nx][ny] # 갈 수 있는 방향의 칸의 번호.
                    if t == -1: # 물고기가 칸에 없다면
                        a = g[x][y]
                        g[nx][ny] = a
                        fish[f][0],fish[f][1] = nx,ny
                        g[x][y] = -1
                    else:
                        g[x][y], g[nx][ny] = g[nx][ny],g[x][y]
                        fish[f][0],fish[f][1] = nx,ny
                        fish[t][0],fish[t][1] = x,y
                
                    break
def candidate():
    global shark
    arr = []
    x,y,d = shark
    nx = x
    ny = y
    
    while True:

        nx += dx[d]
        ny += dy[d]
        
        if 0 <= nx < 4 and 0 <= ny < 4:
            if g[nx][ny] != -1: # 물고기가 있다면,
                arr.append((nx,ny))
        else:
            break
    
    return arr

def dfs(total):
    global answer, shark
    
    answer = max(answer,total)
    fishM()
    print(g)
    arr = candidate()
    if len(arr) == 0: # 상어가 이동할 수 있는 칸이 없다면.
        return
    
    for x,y in arr:
        
        tx,ty,td = shark
        num = g[x][y]
        
        tmp = fish[num][:]

        shark = [x,y,fish[g[x][y]][2]]
        g[x][y] = -1
        fish[g[x][y]] = [-1,-1,-1]
        
        dfs(total+num)

        fish[num] = tmp[:]
        g[x][y] = num
        shark = tx,ty,td

dfs(answer)
print(answer)