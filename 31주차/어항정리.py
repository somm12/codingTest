import copy
n,k = map(int,input().split())
arr = list(map(int,input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

fish = [[i] for i in arr]
cnt = 0
def check(): # 물고기 수가 가장 작은 어항, 가장 큰 어항 차이가 k이하인지 체크.
    tmp = []
    for i in fish:
        for j in i:
            tmp.append(j)
    maxV = max(tmp)
    minV = min(tmp)
    if (maxV-minV) <= k:
        return True

    return False

def putFish():# 제일 물고기 수가 작은 모든 어항에 물고기 1마리 추가.
    global fish
    tmp = []
    for i in fish:
        for j in i:
            tmp.append(j)
    minV = min(tmp)
    for i in fish:
        if i[0] == minV:
            i[0] += 1

def build(): # 가장 왼쪽어항을 그 오른쪽 어항위로 쌓기
    global fish
    left = fish.pop(0)
    fish[0].append(left[0])

def rotate90():# 2개 이상인 어항 전체 공중 부양 시켜서 90도 시계 방향 회전후 쌓기.
    global fish
    tmp = []
    # 공중 부양할 어항(2개이상 쌓인 것)들을 tmp에 담는다.
    while True:
        if fish and len(fish[0]) > 1:
            tmp.append(fish.pop(0))
        else:
            break
    # 공중부양한 전체 어항의 가장 오른쪽 어항 밑에 바닥이 없다면(공주부양 후, 위에 올라갈 면적 > 남은 fish 면적) 반복 멈추기.
    if len(tmp[0]) > len(fish): 
        fish = tmp+fish # ** 90회전 후 쌓기 그만할 때, 현재 fish상태가 pop 했기 때문에, 원래 어항부분이 사라진 상태라서 다시 합친다.
        return False

    while tmp: # 그렇지 않으면 남은 어항위로 쌓는다.
        arr = tmp.pop()
        for i in range(len(arr)):
            fish[i].append(arr[i])
    return True

def control(): # 물고기 수 조절. 인접한 물고기 동시에 모두 d = 차이//5 > 0 일 때, 많은곳->적은고 d가 이동
    global fish
    
    new = copy.deepcopy(fish)
    visited= [] # 이미 인접한 두 물고기 방문을 했는지 체크.
    for x in range(len(fish)):
        for y in range(len(fish[x])):
            for i in range(4):
                nx = x + dx[i] # 상하좌우 검사
                ny = y + dy[i]
                # ** fish[nx]
                if 0 <= nx < len(fish) and 0 <= ny < len(fish[nx]) and (x,y,nx,ny) not in visited:
                    
                    a = fish[x][y]
                    b = fish[nx][ny]
                    
                    v = abs(a-b)
                    d = v//5
                    if d > 0:
                        if a > b:
                            new[x][y] -= d
                            new[nx][ny] += d
                        elif a < b:
                            new[x][y] += d
                            new[nx][ny] -= d
                        
                        visited.append((x,y,nx,ny)) # (x,y)와 (nx,ny) 두 어항 끼리 이동했음을 체크.
                        visited.append((nx,ny,x,y)) # (nx,ny) 와 (x,y) 동일하므로, append함
    fish = new

def oneLine():# 다시 일렬로 어항 배치.
    global fish
    new = []
    for i in fish:
        for j in i:
            new.append([j])
    fish = new

def rotate180(): # 2번 180 돌려서 위로 쌓기.
    global fish
    for _ in range(2):
        left = fish[:len(fish)//2]
        left.reverse()
        for i in left:
            i.reverse() # 여기까지 n//2 left배열 전체, 쌓인 요소 모두 reverse
        fish = fish[len(fish)//2:]
        
        for i in range(len(left)):
            for j in range(len(left[i])): # 위로 쌓기
                fish[i].append(left[i][j])


while True:
    if check():# 가장 큰, 가장 작은 물고기 수 차이가 K이하인지 체크.
        break
    putFish() # 가장 물고기 수 작은 어항들에 물고기 한마리 넣기
    
    build() # 가장 왼쪽 -> 오른쪽 위로 쌓기.
    
    while True:
        if rotate90(): # 밑바닥이 없어지기 전까지, 2개이상 쌓인 어항 전체를 시계방향 90도 회전 후, 위로 쌓는다.
            continue
        else:
            break
    control()# 인접한 어항사이 물고기 수 조절.
    
    oneLine()# 일렬로 만들기
    
    rotate180()# n//2 만큼 시계방향 180 회전 2번.
    
    control()# 물고기 수 조절.
    
    oneLine()# 일렬로 만들기
    
    cnt += 1# 어항정리 횟수 1 증가.
print(cnt)