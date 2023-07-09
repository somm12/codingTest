n, L = map(int,input().split())
answer = 0
arr= []
for _ in range(n):
    arr.append(list(map(int,input().split())))


def isRoad(arr):
    area = 1
    idx = 0
    while idx < n - 1:
        h = arr[idx]
        if h > arr[idx+1]: # 내리막길
            diff =h-arr[idx+1]
            if diff != 1:# 차이가 1인가
                return False
            cnt = 0
            for i in range(idx+1,n): # 연속해서 같은 높이가 L개 이상인가
                if arr[idx+1] == arr[i]:
                    cnt += 1
                else:
                    break
            if cnt >= L:
                idx = idx + L # idx+L까지 건널 수 있고, 그 다음 칸 확인을 해야하므로, area = 0.
                area = 0 
                continue
            else:
                return False
        elif h < arr[idx+1]:# 오르막길
            if arr[idx+1] - h == 1 and area >= L: # L개 이상 and 높이차가 1.
                idx += 1
                area = 1
                continue
            else:
                return False
        else:
            area += 1
            idx += 1
    return True 
# 각 행에 대해서 길인지 확인.
for i,v in enumerate(arr):
    if isRoad(v):
        answer += 1
# 배열을 회전 시키기.
rotate = [[0]*n for _ in range(n)] 
for i in range(n):
    for j in range(n):
        rotate[j][n-i-1] = arr[i][j]
# 각 열에 대해서 길인지 확인
for i,v in enumerate(rotate):
    if isRoad(v):
        answer += 1
print(answer)

# 시뮬레이션 처럼 풀기.