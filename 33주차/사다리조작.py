n,m,h = map(int,input().split())
line = [[False]* (n+1) for _ in range(h+1)]
answer = 4

for _ in range(m):
    a,b = map(int,input().split())
    line[a][b] =True

def check():
    
    for i in range(1,n):
        now = i # column dnlcl
        for j in range(1,h+1):
    
            
            if line[j][now-1]:
                now -= 1
            elif line[j][now]:
                now += 1
            
        if now != i:
            return False
    return True
cnt = 0
def makeLine(total,x,y):
    global line, answer,cnt
    if check():
        cnt += 1
        answer = min(total,answer)
        return
    if total >= answer or total >= 3:
        return
    
    
    for i in range(x,h+1):
        if x == i:
            col = y
        else:
            col = 1

        for j in range(col,n):
            if not line[i][j-1] and not line[i][j] and not line[i][j+1]:
                line[i][j] = True
                makeLine(total+1, i,j+2) 
                line[i][j] = False
makeLine(0,0,0)
if answer > 3:
    print(-1)
else:
    print(answer)
print(cnt)