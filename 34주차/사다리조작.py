n,m,h = map(int,input().split())
line = [[False]*(n+1) for _ in range(h+1)]
answer = 4

def check(): # 모두 i번 -> i번으로 도착하는지 확인하는 함수.
    for x in range(1,n): # 열
        now = x
        for row in range(1,h+1):# 행
            if line[row][now-1]: # 왼쪽에 사다리가 있다면 왼쪽이동.
                now -= 1
            elif line[row][now]: # 오른쪽에 사다리가 있다면 오른쪽 이동.
                now += 1
        if now == x: # i번에서 i번 도착하면 계속
            continue
        else: # 아니라면 False 반환
            return False
    return True

def dfs(total,x,y):# dfs로 최대 3개의 사다리를 추가로 놓아서 조건에 만족되는지 체크.
    global line,answer
    if check(): # 조건이 만족되면
        answer = min(answer,total) # 최솟값 업데이트 후 종료
        return
    if total >= 3 or answer <= total: # 최댓값인 3이상 또는, 이미 구해진 답보다 total 값이 그 이상이면 더이상 탐색하지 않는다.
        return 

    for i in range(x,h+1): # (1,1부터 탐색 시작.)
        if x == i: # 같은 행 탐색 중이라면, 이어서 y 탐색.
            col = y
        else:
            col = 1 # 만약 다른 행 탐색이라면, 다시 column은 1부터 탐색.
        for j in range(col,n):
           
            if not line[i][j-1] and not line[i][j+1] and not line[i][j]:
                line[i][j] = True
                dfs(total+1,i,j+2)
                line[i][j] = False
        
           


for _ in range(m):
    a,b= map(int,input().split())
    line[a][b] = True
dfs(0,1,1)
if answer > 3:
    print(-1)
else:
    print(answer)