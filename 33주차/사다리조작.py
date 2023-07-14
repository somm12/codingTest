n,m,h = map(int,input().split())
line = [[False]* (n+1) for _ in range(h+1)]
answer = 4

for _ in range(m):
    a,b = map(int,input().split())
    line[a][b] =True

def check():
    
    for i in range(1,n):
        now = i # i번 사다리 시작.
        for j in range(1,h+1): 
            if line[j][now-1]:# 왼쪽에 사다리가 있다면 왼쪽이동
                now -= 1
            elif line[j][now]:# 오른쪽에 있으면 오른쪽 이동
                now += 1
            
        if now != i:# i -> i가 아니라면 False 반환.
            return False
    return True

def makeLine(total,x,y):
    global line, answer,cnt
    if check():# 모두 i번 -> i번이라면 update.
        answer = min(total,answer)
        return
    if total >= answer or total >= 3: # 이미 현재 answer이상이라면, 종료.
        return
    
    
    for i in range(x,h+1):
        if x == i: # 현재 탐색하는 부분이 행이 그대로 이어진다면, 열부분은 이어서 탐색.
            col = y
        else: # 현재 탐색하는 부분에서 행이 변경되면, 열부분은 다시 처음부터 탐색.
            col = 1

        for j in range(col,n):
            # 현재 i번 라인에 j번 세로줄에 가로선을 만들려면, 접하지 않아야하며! 옆 선과 이어지면 안됌. 
            # 왼쪽과 오른쪽에도 선이 없는가 체크.
            if not line[i][j-1] and not line[i][j] and not line[i][j+1]:
                line[i][j] = True
                makeLine(total+1, i,j+2) 
                line[i][j] = False
makeLine(0,0,0)
if answer > 3: # 3보다 크게 나오면, -1.
    print(-1)
else:
    print(answer)
