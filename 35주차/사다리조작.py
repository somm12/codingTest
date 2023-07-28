answer = 4 # 최대 3개까지 설치 가능하기 때문에 큰 값 4를 할당.
n,m,h = map(int,input().split())# 열, 가로선 개수, 행 입력.
line = [[0]* (n+1) for _ in range(h+1)]# 1번 ~ n번 열, 1~h번 행.

for _ in range(m):
    a,b = map(int,input().split())
    line[a][b]=1 # a번행의 b열와 b+1열이 연결 되있음.

def check():# 모든 1~n번이 i -> i 로 도착하는지 체크.
    for x in range(1,n+1):
        now = x # 현재 i번 시작점.
        for r in range(1,h+1): # row 한칸씩 내려감.
            if now > 1 and line[r][now-1]:# 만약 왼쪽에 사다리가 있다면 이동.
                now -= 1
            elif line[r][now]:# 만약 오른쪽에 사다리가 있다면 이동
                now += 1
        if x == now:# 이동후에 i -> i 번이라면, 계속 진행
            continue
        else: # 하나라도 아니라면 False 반환.
            return False

    return True # 모두 i-> i번도착 True .

def dfs(total,x,y):# 추가할 사다리 개수 세기
    global answer,line
    if check(): # 모두 i -> i번 도착인지 체크.
        answer = min(answer,total) # answer update.
        return
    
    if total >= 3 or total>=answer: # 만약 현재까지 세는 개수가 3 이상이라면 그만두기, 또는 이미 answer 이상으로 크다면 그만.
        return
     
    for i in range(x,h+1):# 행
        if x == i:
            col = y # 아직 같은 행 검사 중이라면, 매개변수 이어서 y할당
        else:
            col = 1 # 백트래킹으로 다음 행 검사를 한다면, 열은 1부터 다시 탐색.
        for j in range(col,n):# 가로선이 이어지면 안되므로, 체크.
            if not line[i][j] and not line[i][j-1] and not line[i][j+1]:
                line[i][j] =1 # 선택.
                dfs(total+1,i,j+2) # 다 다음 열부터 탐색 가능.
                line[i][j] = 0 # 백트래킹으로 다시 0 할당.
dfs(0,1,1) # (1,1)부터 선택 시작! => 전체 가능한 것 중에서 최대 3개를 뽑는 것이므로 조합. 조합은
# 매개변수에 인덱스를 넣으면서 범위를 좁혀간다.
if answer > 3: # 3보다 크면 -1
    print(-1)
else:
    print(answer)

