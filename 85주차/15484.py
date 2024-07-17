
N,M,H = map(int,input().split())
g = [[0]*(N+1) for _ in range(H+1)]# 1부터 행, 1부터 열이 시작.
for _ in range(M):
    a,b = map(int,input().split())
    g[a][b] = 1
arr = []
answer = int(1e9)# 최댓값 최기화.
def check():# i -> i로 나오는지 체크.
    
    for num in range(1,N+1):
        pos = num
        for row in range(1,H+1):
            if g[row][pos]:
                pos += 1
            elif pos > 1 and g[row][pos-1]:
                pos -= 1
        if pos != num:
            return False
    return True

def go(L,x,y):
    global g, answer
    if check():
        answer = min(answer,L)
        return
    if answer <= L or L >= 3:# 이미 최소값이 존재하면 종료, check한 이후에도 3개 넘게 사다리를 요구하므로 종료.
        return
    for i in range(x,H+1):
        if x == i:# 같은 행에서 선택 할 수 있을 때
            y= y
        else:# 다음 행에서 선택해야할 때는 다시 열은 첫번째 부터 고르기.
            y = 1
        for j in range(y,N):
            if g[i][j] == 0 and g[i][j-1] == 0 and g[i][j+1]== 0:# 겹치거나, 양 옆에 사다리가 연속되면 안됨.
                g[i][j] = 1
                go(L+1,i,j+2)# 다 다음 열부터 선택 가능.
                g[i][j] = 0



go(0,1,1)
if answer == int(1e9):
    print(-1)
else:
    print(answer)

# 백준 사다리 조작.