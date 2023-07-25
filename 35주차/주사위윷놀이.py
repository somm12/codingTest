score= [0,2,4,6,8,10,
12,14,16,18,20,
22,24,26,28,30,
32,34,36,38,40,
13,16,19,25,22,
24,28,27,26,30,
35,0]

next = [[1],[2],[3],[4],[5],[6,21],
[7],[8],[9],[10],[11,25]
,[12],[13],[14],[15],[16,27],
[17],[18],[19],[20],[32],
[22],[23],[24],[30],
[26],[24],[28],[29],[24],
[31],[20],[32]]

dice = list(map(int,input().split()))
horse = [0,0,0,0]
answer = 0
def dfs(L,total):
    global answer
    if L == 10:
        answer = max(answer,total)
        return
    for i in range(4):
        if horse[i] != 32:
            x = horse[i]
            if len(next[x]) == 2:
                x = next[x][1]
            else:
                x = next[x][0]
            for _ in range(dice[L]-1):
                x = next[x][0]
            
            if (x == 32) or x not in horse:
                prev = horse[i]
                horse[i] = x
                dfs(L+1, total+ score[x])
                horse[i]= prev

dfs(0,0)
print(answer)