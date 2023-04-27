
def dfs(L):
    global answer
    if L == n*m:
        answer += 1
        return
    
    x = L//m + 1
    y = L%m +1
    # 넴모넴모 배치 X 경우.
    dfs(L+1)

    # 배치하는 경우 : 2x2가 생기지 않는 경우 조건 확인 후 배치하기.
    if check[x][y-1] ==0 or check[x-1][y] == 0 or check[x-1][y-1] == 0:
        check[x][y] = 1
        dfs(L+1)
        check[x][y] = 0
    
    
            
n,m=map(int,input().split())
check = [[0]*(m+1) for _ in range(n+1)]
answer = 0
if m < 2:
    print(2**(n*m))
else:
    dfs(0)
    print(answer)