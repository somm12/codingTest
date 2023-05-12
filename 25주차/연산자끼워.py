n = int(input())
arr = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
minV = int(1e9) # 최솟값을 담을 변수
maxV = -int(1e9) # 최댓값을 담을 변수

def dfs(L, total, add, minus, mul, div):
    global minV, maxV
    if L == n-1: # n-1개의 연산자를 모두 연산하면, 최솟값 최댓값 업데이트
        maxV = max(maxV, total)
        minV = min(minV, total)
        return
    if add > 0: # 매개변수를 통해 값을 계산하고 각 연산자의 개수를 -1 씩 하기.
        dfs(L+1,total+arr[L+1],add-1,minus,mul,div)
    if minus > 0:
        dfs(L+1, total-arr[L+1],add, minus-1,mul,div)
    if mul >0:
        dfs(L+1, total*arr[L+1],add,minus,mul-1,div)
    if div > 0:
        dfs(L+1, int(total/arr[L+1]),add,minus,mul,div-1)
dfs(0,arr[0],a,b,c,d)
print(maxV)
print(minV)