n = int(input())
arr = list(map(int,input().split()))
minV = int(1e9)
maxV = -int(1e9)

add,minus,mul,div = map(int,input().split())
def dfs(L,add,minus,mul,div,total):
    global minV,maxV
    
    if L == n:
        minV = min(minV,total)
        maxV = max(maxV,total)
        return
    if L == 0:
        dfs(L+1, add,minus,mul,div,total+arr[L])
    else:
        if add > 0:
            dfs(L+1, add-1,minus,mul,div,total+arr[L])
        if minus > 0:
            dfs(L+1, add,minus-1,mul,div,total-arr[L])
        if mul > 0:
            dfs(L+1, add,minus,mul-1,div,total*arr[L])
        if div > 0:
            if total < 0:
                dfs(L+1, add,minus,mul,div-1,(abs(total)//arr[L]) * -1)
            else:
                dfs(L+1, add,minus,mul,div-1,total//arr[L])
                
dfs(0,add,minus,mul,div,0)      
print(maxV)
print(minV)
# 백준 연산자 끼워놓기.
# 연산자가 나올 수 있는 전체 경우의 수 => 4^10 == 2^20 