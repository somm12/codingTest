n,k = map(int,input().split())
import copy
dx = [-1,1,0,0]
dy = [0,0,-1,1]
fish = list(map(int,input().split()))
fish = [[v] for v in fish]

time = 0

def leastFish(minV):
    global fish
    for i,v in enumerate(fish):
        if v[0] == minV:
            fish[i][0] += 1
def build():
    global fish
    left = fish[0][0]
    right = fish[1:]

    right[0].append(left)
    fish = right
def rotate90():
    global fish
    while True:
        for i in range(len(fish)-1,-1,-1):
            if len(fish[i]) > 1:
                idx = i
                break
        left = fish[:idx+1]
        right = fish[idx+1:]

        if len(left[-1]) > len(right):
            break

        left.reverse()
        for arr in left:
            for i,v in enumerate(arr):
                right[i].append(v)
        fish = right
def control():
    global fish
    visited = {}
    tmp = copy.deepcopy(fish)
    for x in range(len(fish)):
        for y in range(len(fish[x])):
            if not (x,y) in visited:
                visited[(x,y)] =1
                for i in range(4):
                    nx = x+dx[i]
                    ny = y +dy[i]
                    if not (nx,ny) in visited and 0 <= nx < len(fish) and 0 <= ny < len(fish[nx]):
                        a = fish[nx][ny]
                        b = fish[x][y]
                        d = abs(a-b)//5
                        if d > 0:
                            if a>b:
                                tmp[nx][ny] -= d
                                tmp[x][y] += d
                            else:
                                tmp[nx][ny] += d
                                tmp[x][y] -= d
    fish = tmp # 바뀐 물고기수 반영. fish update
def oneLine():
    global fish
    tmp  =[]
    for arr in fish:
        for v in arr:
            tmp.append([v])
    fish = tmp

def rotate180():
    global fish

    for _ in range(2):
        left = fish[:len(fish)//2] 
        right = fish[len(fish)//2:]
        
        left.reverse()
        i = 0
        for arr in left:
            for v in arr[::-1]: 
                right[i].append(v)
            i +=1
           
        fish = right
while True:
    maxV = -1
    minV = int(1e9)
    for arr in fish:
        maxV = max(maxV,arr[0])
        minV = min(minV, arr[0])
    if maxV - minV <= k:
        print(time)
        break
    # 어항 정리
    leastFish(minV) # 가장 물고기 수가 적은 어항에 +1
    build() # 가장 왼쪽 어항을 오른쪽 어항에 쌓기
    rotate90() # 90도 회전. 쌓인 높이가 바닥에 있는 어항길이보다 커지기 전까지
    control() # 물고기 수 조절
    oneLine() # 다시 일렬로 만들기
    rotate180() # 어항 길이//2 자른 어항을 180 도 2번 회전해서 쌓기
    control() # 물고기수 조절
    oneLine() # 다시 일렬로.
    time +=1
