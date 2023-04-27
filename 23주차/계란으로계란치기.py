def dfs(now,egg):
    global answer
    if now == n:
        tmp = 0
        for i in range(n):
            if egg[i][0] <= 0:
                tmp += 1
        answer= max(answer,tmp)
        return
    
    if egg[now][0] <= 0:# 또는 현재 손에 든 계란이 깨졌다면,
        dfs(now+1,egg)
        return

    allbroken = True
    for i in range(n):
        if i != now and egg[i][0] > 0:
            allbroken = False
            break
    if allbroken:# 자신을 제외한 다른 계란 모두 깨졌다면.
        answer = max(answer, n-1)
        return
        
    # if egg[now][0] <= 0:# 또는 현재 손에 든 계란이 깨졌다면,
    #     dfs(now+1,egg)
    #     return
    
    for i in range(n):
        if i != now and egg[i][0] > 0:
            egg[now][0] -= egg[i][1]
            egg[i][0] -= egg[now][1]
            dfs(now+1,egg)
            egg[now][0] += egg[i][1]
            egg[i][0] += egg[now][1]
                    
    
   
n = int(input())
egg = []
for _ in range(n):
    egg.append(list(map(int,input().split())))
answer = 0
dfs(0,egg)
print(answer)