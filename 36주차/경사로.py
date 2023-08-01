arr = []
n,L = map(int,input().split())
for _ in range(n):
    arr.append(list(map(int,input().split())))
answer =0
def rotate(): # 각 열도 길인지 확인하기 위해서 배열 돌리기.(90도 회전)
    global arr
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-1-i] = arr[i][j]
    arr = new

def check(row):# 현재 배열이 길인지 체크하는 함수.
    idx = 0 # 현재 위치를 나타내는 인덱스 위치.
    now = row[0] # 현재 위치 바로 전 높이
    cnt = 0 # L개인지 알기위해서 개수 세기 위한 변수.
    while True:
        if idx >= len(row):# idx범위 넘어가면 반복문 끝.
            break
        if now == row[idx]: # 이전 높이와 현재 높이가 같다면 개수 늘리기, 다음 인덱스로 넘어감.
            cnt += 1
            idx += 1
        else:# 길이가 서로 다를 때
            if now < row[idx]:  # 다음 위치가 더 높다면 ( 낮은곳 -> 높은곳)
                if row[idx] - now == 1 and cnt >= L: # 차이가 1이고, L개 이상인지 체크.
                    now = row[idx] # 다시 새로워진 높이를 할당.
                    cnt = 1 # 개수는 다시 1로
                    idx += 1 # 위치 update
                else:
                    return False
            else:# 높은곳 -> 낮은곳
                if now - row[idx] == 1: # 차이가 1 이어야하며
                    tmp = 0
                    h= row[idx]
                    for i in range(idx,len(row)):# 이후에 연속되는 낮은칸이 L개이상인지 확인
                        if row[i] == h:
                            tmp += 1
                        else:
                            break
                    if tmp >= L:# L개이상이라면, 다음을 위해 idx위치는 L더해서 update. now. cnt 업데이트(L개까지 자른 것이므로, 개수는 0이 된다.)
                        now = row[idx]
                        idx += L
                        cnt = 0
                        
                    else:# L개 연속이 아니면
                        return False
                else:# 높이차이가 1이 아니면
                    return False
    return True #위의 모든 조건을 통과하는 배열이면 True
                
for row in arr:# 각 행을 확인
    if check(row):
        answer +=1

rotate()

for row in arr:# 각 열이 길인지 확인
    if check(row):
        answer += 1

print(answer)
