n = int(input())
g = []
answer = int(1e9)
for _ in range(n):
    g.append(list(map(int,input().split())))
def dfs(L,res,start): # 조합 구하기.
    if L == n//2: # n//2 만큼 팀이 모이면 능력치 계산 함수 호출.
        calc(res)
        return
    for i in range(start,n): # 조합 만들기
        dfs(L+1,res+[i],i+1)

def calc(arr):
    global answer
    s = {} # 스타트팀
    l = {} # 링크 팀
    for i in arr:
        s[i] = 1
    for i in range(n): # 스타트 팀에 속한 번호 제외한 링크 팀 만들기.
        if not i in s:
            l[i] =1
    
    a= 0
    # 스타트팀의 능력치 계산
    for i in s:
        for j in s:
            a += g[i][j]
    b = 0
    # 링크팀의 능력치 계산
    for i in l:
        for j in l:
            b+= g[i][j]
    answer = min(answer,abs(a-b)) # 능력치 차이 최솟값 업데이트

dfs(0,[],0)
print(answer)