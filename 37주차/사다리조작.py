n,m,h = map(int,input().split())
line = [ [0]*(n+1) for _ in range(h+1)]

for _ in range(m):
    a,b= map(int,input().split())
    line[a][b] =1

answer = 4

def check():
    global line
    for i in range(1,n):# 세로선.
        now = i
        
        for j in range(1,h+1):# 행. 가로선.
           
            if line[j][now-1]:
                now -= 1
            elif line[j][now]:
                now += 1
        if now == i:
            continue
        else:
            return False
    return True
def dfs(total, x,y):
    global answer, line

    if total >= answer or total > 3:
        return
    
    if check():
        answer = min(total,answer)
        return
    for i in range(x,h+1):
        if i == x:
            y = y
        else:
            y = 1
        for j in range(y,n):
            if not line[i][j] and not line[i][j-1] and not line[i][j+1]:
                line[i][j] =1
                dfs(total+1,i,j+2)
                line[i][j] = 0
    


dfs(0,1,1)
if answer > 3:
    print(-1)
else:
    print(answer)
# 사다리 조작 복습.