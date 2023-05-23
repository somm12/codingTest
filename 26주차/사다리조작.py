import sys
input = sys.stdin.readline
n,m,h = map(int,input().split())

line = [[False]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a,b = map(int,input().split()) # a번째 가로줄(1~h), b 와 b+1(1~n) 번째 세로줄 사이에 선이있음.
    line[a][b] = True

answer = 4 # 최솟값을 담을 변수.
candidates = [] # 만들 수 있는 선을 담을 배열. (** 연속으로 선이 만들어지지 않아야함.)
for i in range(1,h+1):
    for j in range(1, n):# b와 b+1 사이 선이므로, 범위는 n-1까지 해야 index out of range 피함.
        if line[i][j] == False and line[i][j-1] == False and line[i][j+1] == False:
            candidates.append((i,j))

def check(line): # 현재의 line 상태로 모두 i -> i 인지 확인. T/F 반환.
    for i in range(1,n+1):
        now = i
        for j in range(1,h+1):
            if line[j][now]: # 오른쪽에 선이 있는지 확인.
                now += 1
            elif line[j][now-1]: # 왼쪽에 선이 있는지 확인.
                now -= 1
        if now != i: # 하나라도 i -> i 로 도착못하면 False.
            return False
    return True

def makeLine(L,line,start):# 후보 중에서 0 ~ 3개까지 선택하면서 i->i 만족하는지 확인.
    global answer
    if L > 3: # 3개가 넘으면 멈추기.
        return
    if answer <= L: # 이미 answer가 현재 depth이하라면, 이후에 depth가 증가해서 더 볼 필요가 없음
        return
    if check(line): # 0 ~ 3개까지 확인 후, i->i 만족하면 answer update. L은 즉, 추가한 사다리개수.
        answer = min(answer,L) # 이어서 L+1가 되므로, 이어서 더 탐색하지 않는다.
        return
    
    for i in range(start, len(candidates)): # 후보 중 하나를 고르기.(조합)
        a,b = candidates[i]
        # 연속적인 선이 되지 않는지 확인.
        if not line[a][b] and not line[a][b+1] and not line[a][b-1]: 
            line[a][b] = True
            makeLine(L+1, line, i+1)
            line[a][b] = False

if m == 0:
    print(0)
else:
    makeLine(0,line,0)
    if answer <=3: # 최솟값이 3개이하면 출력.
        print(answer)
    else:# 3개로 안된다면 -1 출력.
        print(-1)