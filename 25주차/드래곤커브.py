n = int(input())
dict = {}
answer = 0
# x좌표는 좌우로 이동, y좌표는 상하로 이동.
dx = [1,0,-1,0] # 우 상 좌 하
dy = [0,-1,0,1]
# 0 1 2 3 방향을 가지고, 각 세대 규칙을 찾는 함수.
def rule():
    global dict
    # 규칙 찾기.
    arr = [d] # 처음 위치.
    # 규칙은-> 0, 0 1 , 0 1 2 1,,,,([이전 세대] + [이전 세대 방향 +1 거꾸로 한 배열. 3일 때는 0.])
    for _ in range(g): 
        new = []
        for i in arr:
            if i == 3:
                new.append(0)
            else:
                new.append(i+1)
        new.reverse()
        arr += new
    # 모든 좌표 dict에 할당. 한 커브에 대해서 g세대 규칙을 만들었다면, 좌표를 모두 dict에 넣기.
    dict[(x,y)] = 1
    nx = x
    ny = y
    for i in arr:
        nx += dx[i]
        ny += dy[i]
        dict[(nx,ny)]= 1

def check():# 모든 커브가 포함하는 모든 좌표에서 정사각형이 만들어지는지 체크 및 개수 구하기.
    global answer
    for a,b in dict:
        if (a+1,b) in dict and (a,b+1) in dict and (a+1,b+1) in dict:
            answer += 1
for _ in range(n):
    x,y,d,g = map(int,input().split())
    rule()
check()
print(answer)