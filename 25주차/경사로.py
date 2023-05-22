n, L = map(int,input().split())
answer = 0
arr= []
for _ in range(n):
    arr.append(list(map(int,input().split())))

def check(arr): # 현재 배열이 건널 수 있는 길인지 확인. boolean 반환.
    area = 1 # 현재 연속적으로 같은 높이를 가진 칸의 개수.
    idx = 0 # 현재 배열의 인덱스.
    while idx < n - 1: # idx가 n-2일 때까지 확인.
        h = arr[idx] # 현재 칸의 높이.
        if h > arr[idx + 1]:# 다음 칸이 내리막길이라면, 경사로를 두고 지나서 그 다음 idx로 이동.
            area = 0 
            diff = h - arr[idx+1]
            if diff != 1: # 높이 차이가 1인지 확인.
                return False
            next = arr[idx+1]
            cnt  =0
            # 연속적으로 높이가 같은 칸이 L개 이상이라면 idx+L까지 이동가능.
            for i in range(idx+1,n): 
                if arr[i] == next:
                    cnt += 1
                else:
                    break
            if cnt >= L and diff == 1:
                idx = idx + L # 매 반복마다 idx+1의 상태를 파악하므로, idx+L로 이동, area는 다시 0.
                continue
            else:
                return False
        elif h < arr[idx+1]: # 오르막길
            diff = arr[idx+1] - h
            if diff == 1 and area >= L: # 높이가 1인지 확인과 동시에 지금까지 area가 L이상인지 확인.
                area = 1
                idx += 1
                continue
            else:
                return False
        else: # 평평한 길일 때, 면적 +1, 다음 위치로 이동.
            area += 1
            idx += 1
    return True
# 각 행에 대해서 건널 수 있는 길인지 세기
for i,v in enumerate(arr):
    if check(v):
        answer += 1
# 배열을 회전 후, 각 열이 건널 수 있는 길인지 확인
rotate = [[0]*n for _ in range(n)] 
for i in range(n):
    for j in range(n):
        rotate[j][n-i-1] = arr[i][j]
# 각 열에 대해서 건널 수 있는 길인지 세기
for i,v in enumerate(rotate):
    if check(v):
        answer += 1
print(answer)