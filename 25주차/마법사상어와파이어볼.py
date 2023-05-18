from collections import defaultdict
n,M,k = map(int,input().split())
ball = []
dx = [-1,-1,0,1,1,1,0,-1] # 인접한 8방향.
dy = [0,1,1,1,0,-1,-1,-1]
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    ball.append([r-1,c-1,m,s,d])
def move(): # 파이어볼 이동. 이동한 뒤의 파이어볼 정보를 담은 배열 반환.
    after = []
    for x,y,m,s,d in ball:
        nx = x
        ny = y
        for _ in range(s%n): # s칸 이동 -> n으로 나눈 나머지 만큼 이동.
            nx += dx[d]
            ny += dy[d]
        # ** 각 처음과 끝의 행과 열이 연결 되어있음.
        # 만약 이동시, 좌표 범위 초과 방지를 위해서 %n 필수. 음수일 때는 +n
        if nx < 0: 
            nx = -(abs(nx)%n) + n
        else:
            nx = nx%n
        if ny < 0:
            ny = -(abs(ny)%n) + n
        else:
            ny = ny%n
        after.append([nx,ny,m,s,d])
    
    return after

def make(): # 한칸에 두 개이상 파이어볼이 존재할 때, 4개로 나누고 바뀐 전체 파이어볼의 정보 배열 반환.
    # tmp = {(r,c): [[m,s,d],[m,s,d],,]}
    tmp = defaultdict(list) # r-1,c-1 칸에 대해서 존재하는 모든 파이어볼들의 m,s,d 배열을 담는 변수
    # 바뀐 파이어볼 정보를 담은 change
    change= defaultdict(list) # 한 칸에 2개 이상있는 파이어볼들을 4개로 나누어 처리 후에 새로운 해당 파이볼들의 정보
    result = [] # 바뀐 파이어볼(여러개 존재) + 이미 존재한 파이어볼(칸에 한개만 존재) 모두 합친 배열.
    
    for x,y,m,s,d in ball:# 전체 정보를 tmp에 할당.
        tmp[(x,y)].append([m,s,d])
    
    for r,c in tmp:
        if len(tmp[(r,c)]) > 1: # 한 칸에 여러개 일때.
            cnt = len(tmp[(r,c)])
            totalM = 0
            totalS = 0
            totalD = 0
            for m,s,d in tmp[(r,c)]: # 전체 질량 및 속력 합 구하기.
                totalM += m
                totalS += s
                if d % 2== 0:# 모든 방향이 짝수 또는 홀수 인지 구하기 위함.
                    totalD +=1
                else:
                    totalD -= 1
            if totalM//5 == 0: # 질량이 0이면 소멸.
                continue
            if totalD == cnt or totalD == -cnt: # 모든 방향이 짝수 나 홀수라면.
                for j in range(8):
                    if j % 2 == 0: # 0,2,4,6
                        change[(r,c)].append([totalM//5,totalS//cnt,j])
            else: # 아니라면 1,3,5,7
                for j in range(8):
                    if j % 2 != 0:
                        change[(r,c)].append([totalM//5,totalS//cnt,j])
    for r,c in tmp:# 한 칸에 파이어볼이 1개일 때의 경우를 최종 result에 합치기.
        if len(tmp[(r,c)]) == 1:
            m,s,d = tmp[(r,c)][0]
            result.append([r,c,m,s,d])
    for r,c in change: # 한 칸에 파이볼이 2개이상 일때, 4개로 나누어 처리된 파이볼들 result에 합치기
        for m,s,d in change[(r,c)]:
            result.append([r,c,m,s,d])
    
    return result # 바뀐 파이어볼 배열 반환.

answer = 0
for _ in range(k): # k번 실행.
    ball = move()
    ball = make()
for i in ball: # 최종 질량 합치기.
    answer += i[2]
print(answer)
