score = [0,2,4,6,8,10,
12,14,16,18,20,
22,24,26,28,30,
32,34,36,38,40,
13,16,19,25,
28,27,26,22,24,
30,35,0] 

next = [[1],[2],[3],[4],[5],
[6,21], [7],[8], [9], [10],[11,28],
[12],[13],[14],[15], [16,25], 
[17], [18], [19], [20], [32],
[22],[23],[24], [30],
[26], [27], [24], [29] , [24],
[31], [20], [32]]

dice = list(map(int,input().split()))

answer = 0
def dfs(L,total, horse):
    global answer
    if L >= 10:
        answer = max(answer,total)
        return
    for i in range(4):
        if horse[i] != 32: # 도착 칸 아닌 것 중에서 고르기.
            x = horse[i]
            if len(next[x]) == 2: # 파란칸에 있다면, 파란 화살표로 이동.
                x = next[x][1]
            else:
                x = next[x][0]
            for _ in range(1,dice[L]):
                x = next[x][0]
            
            if x == 32 or (x != 32 and x not in horse):
                prev = horse[i]
                horse[i] = x
                dfs(L+1,total+score[x], horse)
                horse[i] = prev # 백트래킹
dfs(0,0,[0,0,0,0])
print(answer)

# 각 점수가 다음으로 가리키는 점수를 해당 인덱스 배열로 표현하는 것 **.