n = int(input())
g = [[0]*(n+1)]
for _ in range(n):
    a = [0]
    arr = list(map(int,input().split()))
    g.append(a+arr)

def drawLine(x,y,d1,d2): # 경계선 구하기.
    tmp = [[0]*(n+1) for _ in range(n+1)]
    
    nx = x
    ny = y
    while True:
        if nx > x+ d1:
            break
        tmp[nx][ny] = 5
        nx += 1
        ny -= 1
    nx = x
    ny = y
    while True:
        if nx > x+d2:
            break
        tmp[nx][ny] = 5
        nx += 1
        ny += 1
    nx = x+d1
    ny = y -d1
    while True:
        if nx > x+d1+d2:
            break
        tmp[nx][ny] = 5
        nx += 1
        ny += 1
    nx = x + d2
    ny = y + d2
    while True:
        if nx > x+d2+d1:
            break
        tmp[nx][ny] = 5
        nx += 1
        ny -= 1
    return tmp

def divideArea(tmp,x,y,d1,d2):# 1,2,3,4번 구역과 5번 구역 할당.
    
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 1

    for r in range(1,x+d2+1):
        for c in range(n,y+1-1, -1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 2
    
    for r in range(x+d1,n+1):
        for c in range(1,y-d1+d2):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 3
    
    for r in range(x+d2+1,n+1):
        for c in range(n, y-d1+d2 -1, -1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 4
    
    for r in range(1,n+1):
        for c in range(1,n+1):
            if tmp[r][c] == 0:
                
                tmp[r][c] = 5
   
    return tmp

def diff(tmp): # 큰 구역 인구수 - 작은 구역 인구수 차이 구하고 answer update.
    global answer
    arr = [0]*6
    for r in range(1,n+1):
        for c in range(1,n+1):
            arr[tmp[r][c]] += g[r][c]
    
    maxV = max(arr[1:])
    minV = min(arr[1:])
    answer = min(answer,maxV-minV)

def decide():# 기준점과 경계선 정하기.
    for d1 in range(1,n+1):
        for d2 in range(1,n+1):
            for x in range(1,n+1):
                for y in range(1,n+1):
                    if (1 <= x and x < x+d1+d2 and x+d1+d2 <= n and 1<= y-d1 and y-d1 < y and y < y+d2 and y+d2 <= n):
                            tmp = drawLine(x,y,d1,d2)
                            tmp = divideArea(tmp,x,y,d1,d2)
                            diff(tmp)

                        
answer = int(1e9)

decide()
print(answer)