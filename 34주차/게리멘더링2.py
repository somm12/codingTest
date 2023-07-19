n = int(input())
g  = [[0]* (n+1)]
for _ in range(n):
    arr = list(map(int,input().split()))
    arr = [0] + arr
    g.append(arr)

answer = int(1e9)
total  =0
for i in g:
    total += sum(i)

def makeLine(x,y,d1,d2): # !! 범위가 아닌 특정 점들을 구하는 것.
    global tmp
    c=y
    for r in range(x,x+d1+1):
        tmp[r][c] = 5
        c -= 1
    c = y
    for r in range(x,x+d2+1):
        tmp[r][c] = 5
        c += 1
    
    c = y-d1
    for r in range(x+d1,x+d1+d2+1):
        tmp[r][c] = 5
        c += 1
    
    c = y +d2
    for r in range(x+d2, x+d2+d1+1):
        tmp[r][c] = 5

        c -= 1

def area(x,y,d1,d2): # 그린 경계선을 만나면 각 선거구 인구수를 더하는 것을 멈춘다.
    global answer, tmp
    one = 0
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if tmp[r][c] == 5:
                break
            one += g[r][c]
    two = 0
    for r in range(1,x+d2+1):
        for c in range(n,y,-1):
            if tmp[r][c] == 5:
                break
            two += g[r][c]
    three = 0
    for r in range(x+d1, n+1):
        for c in range(1,y-d1+d2):
            if tmp[r][c] == 5:
                break
            three += g[r][c]
    four = 0
    for r in range(x+d2+1,n+1):
        for c in range(n,y-d1+d2-1,-1):
            if tmp[r][c] == 5:
                break
            four += g[r][c]
    arr = [one,two,three,four]
    five = total - sum(arr) # 남은 인구수가 경계선 및 경계선 내의 인구수들의 합.
    arr.append(five)

    diff = max(arr) - min(arr)
    answer = min(diff,answer)

# 경계선, 기준점 정하기.
for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            for y in range(1,n+1):
                if 1 <= x < x + d1+d2 <= n and 1 <= y -d1 <y < y+d2 <= n:
                    tmp = [[0]*(n+1) for _ in range(n+1)] # 경계선을 그릴 임시 2차원 배열.
                    makeLine(x,y,d1,d2)# 경계선 그리기
                    area(x,y,d1,d2)# 각 선거구 지역 인구수 구하기 & 인구수차이 업데이트.
print(answer)