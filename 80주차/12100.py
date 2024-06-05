n = int(input())
g = []
for _ in range(n):
     g.append(list(map(int,input().split())))

def dfs(L,g):
    global answer
    
    if L == 5:
        for arr in g:
            answer = max(answer,max(arr))
        return
    for i in range(4):
        visited =[[0]*n for _ in range(n)]
        tmp = [[0]*n for _ in range(n)]
        if i == 0:# 상
            for y in range(n):
                pos = 0
                for x in range(n):
                    if g[x][y] == 0 or visited[x][y]: continue

                    tmp[pos][y] = g[x][y]
                    for k in range(x+1,n):
                        if g[k][y] != 0:
                            if g[k][y] == g[x][y]:
                                tmp[pos][y] *= 2
                                visited[k][y] = 1
                                visited[x][y] = 1
                            break
                    pos += 1
            
        elif i == 1:#하
            for y in range(n):
                pos = n-1
                for x in range(n-1,-1,-1):
                    if g[x][y] == 0 or visited[x][y]: continue

                    tmp[pos][y] = g[x][y]
                    for k in range(x-1,-1,-1):
                        if g[k][y] != 0:
                            if g[k][y] == g[x][y]:
                                tmp[pos][y] *= 2
                                visited[k][y] = 1
                                visited[x][y] = 1
                            break
                    pos -= 1
        elif i == 2:# 좌
            for x in range(n):
                pos = 0
                for y in range(n):
                    if g[x][y] == 0 or visited[x][y]: continue

                    tmp[x][pos] = g[x][y]
                    for k in range(y+1,n):
                        if g[x][k] != 0:
                            if g[x][k] == g[x][y]:
                                tmp[x][pos] *= 2
                                visited[x][k] = 1
                                visited[x][y] = 1
                            break
                    pos += 1
        elif i == 3:
            for x in range(n):
                pos = n-1
                for y in range(n-1,-1,-1):
                    if g[x][y] == 0 or visited[x][y]: continue

                    tmp[x][pos] = g[x][y]
                    for k in range(y-1,-1,-1):
                        if g[x][k] != 0:
                            if g[x][k] == g[x][y]:
                                tmp[x][pos] *= 2
                                visited[x][k] = 1
                                visited[x][y] = 1
                            break
                    pos -= 1
        dfs(L+1,tmp)
                    

    
answer = 0
dfs(0,g)
print(answer)
# 백준 2048문제
# 더 빠른 코드로 다시 구현 완료.
# 빈 배열로 따로 초기화를 해서, 합쳐진 적이 있는 칸 또는 0일 경우를 제외하고 row 나 column 변수를 증가시켜서 
# 연속적으로 각 이동 방향으로 숫자를 배치 시킬 수 있도록 한다.