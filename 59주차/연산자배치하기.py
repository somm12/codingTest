n = int(input())
arr = list(map(int,input().split()))
minV = int(1e9) + 1
maxV = -int(1e9) - 1
add,minus,mul = map(int,input().split())

op = []
for _ in range(add):
    op.append('+')

for _ in range(minus):
    op.append('-')

for _ in range(mul):
    op.append('*')

visited = [0]*(n-1)

def cal(num,s,L):
    if s == '+':
        return num + arr[L]
    if s == '-':
        return num - arr[L]
    return num * arr[L]

def dfs(total,L):
    global minV, maxV
    if L == n:
        minV = min(total,minV)
        maxV = max(total,maxV)
        return
    for i in range(n-1):
        if not visited[i]:
            visited[i] = 1
            
            v = cal(total,op[i],L)
            dfs(v, L+1)
            visited[i] = 0
dfs(arr[0],1)
print(minV,maxV)

# 조금 더 개선된 풀이.
n = int(input())
arr = list(map(int,input().split()))
minV = int(1e9) + 1
maxV = -int(1e9) - 1
add,minus,mul = map(int,input().split())

def dfs(L,total,add,minus,mul):
    global minV,maxV
    if L == n:# n개 숫자 연산이 끝나면 업데이트
        minV = min(total,minV)
        maxV = max(total,maxV)
        return
    if add > 0:
        dfs(L+1, total+arr[L],add-1,minus,mul)
    if minus > 0:
        dfs(L+1, total-arr[L], add,minus-1,mul)
    if mul > 0:
        dfs(L+1, total*arr[L], add, minus,mul-1)
dfs(1,arr[0],add,minus,mul)
print(minV,maxV)
