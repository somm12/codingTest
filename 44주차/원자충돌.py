from collections import defaultdict
n,m,k = map(int,input().split())
dict = defaultdict(list)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(m):
    x,y,m,s,d = map(int,input().split())
    dict[(x-1,y-1)].append((m,s,d))# dict에 (x,y)좌표에 질량 m, 속력 s, 방향 d를 가진다.

answer = 0

def move():# 각각 d방향으로 s만큼 이동.
    global dict
    tmp = defaultdict(list)
    for x,y in dict:
        for m,s,d in dict[(x,y)]:
            nx = (x+(dx[d]*s)) % n
            ny = (y+(dy[d]*s)) % n
            tmp[(nx,ny)].append((m,s,d))
    dict = tmp

def one():# 한 칸에 2개이상 있는 원자들을 합성하고, 나누는 함수
    global dict
    tmp = defaultdict(list)
    for x,y in dict:
        if len(dict[(x,y)]) <2:
            for m,s,d in dict[(x,y)]:
                tmp[(x,y)].append((m,s,d))
        else:
            totalM, totalS, even, odd, cnt = 0,0,0,0,0
            for m,s,d in dict[(x,y)]:
                cnt +=1
                totalM += m
                totalS += s
                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if totalM >= 5:# 질량이 5이상이어야, 4개 원자로 나누었을 때 소멸되지 않음.
                sm,ss = (totalM//5), (totalS//cnt)
                if even == len(dict[(x,y)]) or odd == len(dict[(x,y)]):# 모두 양수 또는홀수 일때, 상하좌우 방향을 갖는다.
                    for d in [0,2,4,6]:
                        tmp[(x,y)].append((sm,ss,d))
                else:
                    for d in [1,3,5,7]:# 그렇지 않으면 대각선 4방향으로 각각 방향을 할당.
                        tmp[(x,y)].append((sm,ss,d))
    dict = tmp

for _ in range(k):
    move()

    one()
# 남은 원소들 총 질량 구하기
for x,y in dict:
    for m,s,d in dict[(x,y)]:
        answer += m
print(answer)