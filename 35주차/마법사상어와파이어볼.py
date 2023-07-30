from collections import defaultdict
answer = 0
ball = defaultdict(list)
n,m,k = map(int,input().split())
dx =[-1,-1,0,1,1,1,0,-1] # 8가지 방향.
dy = [0,1,1,1,0,-1,-1,-1]
def move():# 파이어볼 모두 이동.
    global ball
    new = defaultdict(list)
    for x,y in ball: 
        for m,s,d in ball[(x,y)]:
            nx = (x+dx[d]*s) # d방향 s칸.
            ny = (y+dy[d]*s) 
            nx %= n # 행 열 모두 연결 됨.
            ny %= n
            new[(nx,ny)].append([m,s,d]) # 옮겨진 위치로 다시 할당.
    ball =new # ball 위치 update.
 
def makeOne():# 2개이상 한칸에 있는 파이어볼 하나로 합치기.
    global ball

    for x,y in ball:
        if len(ball[(x,y)]) >= 2:
            length = len(ball[(x,y)])
            totalM, totalS, even, odd = 0,0,0,0 # 총질량, 속력, 방향이 짝수 홀수인지 확인 위한 변수.
            for m,s,d in ball[(x,y)]:
                totalM += m
                totalS += s

                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if totalM // 5 == 0:# 질량이 0 이면 소멸. del를 쓰면 for반복문에서 ball 이 바뀌므로, 조심.
                ball[(x,y)] = []
                continue
            else:
                ball[(x,y)] = []# 만약 모두 방향이 짝수 또는 홀수라면 0,2,4,6 방향으로 할당.
                if even == length or odd == length:
                    for i in [0,2,4,6]:
                        ball[(x,y)].append([totalM//5, totalS//length,i])
                else:
                    for i in [1,3,5,7]:
                        ball[(x,y)].append([totalM//5, totalS//length,i])
for _ in range(m):# m개 입력
    r,c,m,s,d = map(int,input().split())
    ball[(r-1,c-1)].append([m,s,d])

for _ in range(k):# K번 마법.

    move()
    makeOne()

for x,y in ball:# 총질량합 구하기.
    for m,s,d in ball[(x,y)]:
        answer += m
print(answer)