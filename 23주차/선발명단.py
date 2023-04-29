def dfs(total,L):
    global answer
    if L == 11:
        answer = max(answer,total)
        return
    for i in range(11):
        # 현재 L번째 선수의 i번째 포지션 능력치가 0보다 크고, 해당 포지션에 아무도 배치가 안되었다면
        if players[L][i] > 0 and not visited[i]:
            visited[i] = 1
            dfs(total+players[L][i], L+1)
            visited[i] = 0



c = int(input())
for _ in range(c):
    players = []
    for _ in range(11):
        players.append(list(map(int,input().split())))
    answer = 0
    visited = [0]*11
    dfs(0,0)
    print(answer)