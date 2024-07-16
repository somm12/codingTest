k = int(input())
arr = list(input().split())

maxV = 0
minV = int(1e9)*10
visited = [0]*10

def check(a,b,op):
 
    if op == '<' and a < b:
        return True
    if op == '>' and a> b:
        
        return True
    return False

def dfs(L,ret):
    global minV, maxV
    
    if L == k+1:
        answer.append(ret)
        return

    for i in range(10):
        if L == 0 or (visited[i] == 0 and check(ret[L-1],str(i),arr[L-1])):
            visited[i] = 1
            dfs(L+1,ret + str(i))
            visited[i] = 0
answer =[]
dfs(0,'')
answer.sort()
print(answer[-1])
print(answer[0])

# 완전 탐색. 순열을 만들어가면서 부등호가 맞는지 체크하여 시간 복잡도를 조금씩 줄이기
# 백준 부등호.
