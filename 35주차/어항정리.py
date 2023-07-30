import copy
time = 0
n,k = map(int,input().split())
tmp = list(map(int,input().split()))
fish = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for v in tmp:
    fish.append([v])

def moreFish():
    global fish
    tmp = copy.deepcopy(fish)
    tmp.sort(key=lambda x: x[0])
    
    x = tmp[0][0]
    
    for r in range(len(fish)):
        for c in range(len(fish[r])):
            if fish[r][c] == x:
                fish[r][c] += 1
    
def move():
    global fish
    first = fish[0].pop()
    fish[1].append(first)
    fish.pop(0)

def rotate90():
    global fish
    # 뒤에서 부터 물고기 수가 2개 이상인 어항과 아닌 쪽을 left, right로 나누기.
    for i in range(len(fish)-1,-1,-1):
        if len(fish[i]) >= 2:
            left = fish[:i+1]
            right = fish[i+1:]
            break
    # 바닥에 있는 어항 개수, 공중 부양한 어항 수가 더 커진다면 더이상 90도 회전해서 쌓을 수 없음.      
    if len(left[-1]) > len(right):
        return False
    # 쌓을 때 left 부분에서 뒤쪽 배열 먼저 쌓아지므로, 역순으로 만들기
    for arr in left[::-1]: # arr는 2개이상 쌓인 어항 배열.
        # 한개씩 왼쪽에서 부터 right의 어항 한칸씩 값이 쌓인다.
        idx = 0
        for v in arr:
            right[idx].append(v)
            idx += 1

    fish = right# 쌓여진 right로 fish 업데이트.
   
    return True

def control():# 인접한 어항 물고기 수 조절.
    global fish
    new = copy.deepcopy(fish)# 동시에 조절되므로, fish 을 바로 바꾸기 않기 위해서 new에 값을 복사.
    visited = [[0]*len(fish[0]) for _ in range(len(fish))]# 이미 방문한 어항은 피하기 위한 배열.
    for x in range(len(fish)):
        for y in range(len(fish[x])):
            visited[x][y] =1 # 방문처리.
            for i in range(4):# 인접 방향 상하좌우.
                nx = x+dx[i]
                ny = y+dy[i]
                # 범위 **, 물고기 수 조절시 이미 방문한 물고기는 제외해야하므로, 배열이 모두 column 개수가 같지 않음에 유의
                if 0 <= nx < len(fish) and 0<= ny < len(fish[nx]) and not visited[nx][ny]:
                    a = fish[x][y]
                    b = fish[nx][ny]
                    d = abs(a-b)//5 # d값이 0보다 크면 큰 물고기 수 어항에서 작은 어항으로 d마리 물고기 들어감
                    if d > 0:
                        if a>b:
                            new[x][y] -= d
                            new[nx][ny] += d
                        else:
                            new[x][y] += d
                            new[nx][ny] -= d
                 
    fish = new # 물고기 update
def line():# 한줄로 만들기.
    global fish
    new = []
    for arr in fish:
        for v in arr:
            new.append([v])
    fish = new

def rotate180():# 2번 반을 갈라서 180도 회전해서 쌓기.
    global fish
    for _ in range(2):
        length = len(fish)
        idx = length//2
        left = fish[:idx]
        right = fish[idx:]
        idx = 0
        for arr in left[::-1]: # 180 회전시,거꾸로, 해당 어항내 배열고 거꾸로 역순먼저 쌓인다.
            for v in arr[::-1]:
                right[idx].append(v)
            idx += 1

        fish = right # 연속 두번으로 회전이므로, fish update해주기.


while True:
    maxV = -1
    minV = 10**5
    for arr in fish:# 차이가 k이하면 멈춘다.
        maxV = max(maxV, max(arr))
        minV = min(minV, min(arr))
    if maxV-minV <=k:
        print(time)
        break
    moreFish()
    move()
    while True:
        if not rotate90():
            break
    
    control()

    line()
    rotate180()
    
    control()

    line()
 
    time +=1


