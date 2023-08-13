n = int(input())
g = []
answer = int(1e9)
total = 0
for _ in range(n):
    g.append(list(map(int,input().split())))
 
for i in g:
    total += sum(i)

def drawLine():
    global tmp
    nx,ny = x,y
    while True:
        tmp[nx][ny] = 5
        nx += 1
        ny -= 1
        if nx > x +d1:
            break
    nx,ny = x,y
    while True:
        tmp[nx][ny] = 5
        nx += 1
        ny += 1
        if nx > x +d2:
            break
    nx,ny = x+d1,y-d1
    while True:
        tmp[nx][ny] = 5
        nx += 1
        ny += 1
        if nx > x +d1+d2:
            break
    nx,ny = x+d2, y+d2
    while True:
        tmp[nx][ny] = 5
        nx += 1
        ny -= 1
        if nx > x +d2+d1:
            break

def area():
    global tmp
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 1
    for r in range(1,x+d2+1):
        for c in range(n,y,-1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 2

    for r in range(x+d1,n+1):
        for c in range(1,y-d1+d2):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 3

    for r in range(x+d2+1,n+1):
        for c in range(n,y-d1+d2-1,-1):
            if tmp[r][c] == 5:
                break
            tmp[r][c] = 4

def diff():
    global answer
    arr = [0]*6
    for r in range(1,n+1):
        for c in range(1,n+1):
            if tmp[r][c] != 5 and tmp[r][c]!=0:
                arr[tmp[r][c]] += g[r-1][c-1]
    five = total-sum(arr)
    arr[5] = five
    arr = arr[1:]
    diff = max(arr)-min(arr)
    answer = min(answer, diff)

    
    


for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if x < x+d1+d2 <=n and 1<= y-d1 < y < y+d2 <= n:
                    tmp = [[0]* (n+1) for _ in range(n+1)]
                    drawLine()# 경계선 그리기
                    area()# 1,2,3,4구역 표시
                    diff()# 차이 구하기
                    

print(answer)

# 백준 삼성기출.