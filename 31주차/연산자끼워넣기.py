n = int(input())
arr = list(map(int,input().split()))
add, minus, mul, div = map(int,input().split())
maxV = -int(1e9) # -10억 보다 크거나 같음.
minV = int(1e9) # 10억 보다 작거나 같음 => 범위를 최대, 최소로 미리 할당해두기.

def dfs(L,add,minus,mul,div,res): # 각 덧셈, 뺄셈, 곱셈, 나눗셈이 남은 경우 가지를 뻗어나가고, 앞에서 부터 계산
    global minV,maxV
    if L == n-1:
        maxV = max(maxV,res)
        minV = min(minV,res)
        return
    if add > 0:
        dfs(L+1, add-1, minus,mul,div,res + arr[L+1])
    if minus>0:
        dfs(L+1, add,minus-1,mul,div,res - arr[L+1])
    if mul > 0:
        dfs(L+1, add,minus,mul-1,div,res * arr[L+1])
    if div > 0:
        dfs(L+1, add,minus,mul,div-1,int(res/arr[L+1])) # 음수 / 양수일 때, 조건 처리
dfs(0,add,minus,mul,div,arr[0])
print(maxV)
print(minV)