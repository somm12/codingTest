n = int(input())
g = [[0]*(n+1)]
for _ in range(n):
    tmp = [0]
    tmp += list(map(int,input().split()))
    g.append(tmp)
total = 0
for arr in g:
    for i in arr:
        total += i # 전체 인구수.
answer = int(1e9)
for x in range(1,n):
    for y in range(1,n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if x < x+d1+d2<=n and 1 <= y-d1 <y and y < y+d2 <= n:
                    a = [0]*5

                    tmp = y+ 1 # y의 범위(경계선 전까지)
                    for r in range(1,x+d1):
                        if r >= x:
                            tmp  -= 1
                        for c in range(1,tmp):
                            a[0]+= g[r][c]
                    # 2번
                    tmp = y + 1
                    for r in range(1,x+d2+1):
                        if r > x: # r이 x행을 넘어가면 y 범위가 점점 좁아짐.
                            tmp += 1
                        for c in range(tmp,n+1):
                            a[1] += g[r][c]
                    # 3번
                    tmp = y - d1
                    for r in range(x+d1,n+1):
                        for c in range(1,tmp):
                            if c < y-d1+d2:
                                a[2] += g[r][c]
                        tmp += 1
                    # 4번
                    tmp = y+d2
                    for r in range(x+d2+1,n+1):
                        for c in range(tmp,n+1):
                            if c >= y-d1+d2:
                                a[3] += g[r][c]
                        tmp -= 1
                    # 5번 구역 인구수 구하기. 전체 - 나머지 지역 인구수의 합.
                    a[4] = total - sum(a[:4]) 
                    diff = max(a) - min(a) # 인구수 최대 최소 차이 구하기.
                    answer = min(answer,diff) # 인구 수 차이 update
                    
print(answer)