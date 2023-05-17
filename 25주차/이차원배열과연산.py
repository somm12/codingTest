from collections import defaultdict


r,c,k = map(int,input().split())
t = 0
arr = []
for _ in range(3):
    arr.append(list(map(int,input().split())))
# 행을 기준으로 정렬하는 함수: 숫자가 나온 횟수와 숫자를 횟수 > 숫자 크기 순으로 정렬. 정렬된 배열 반환.
def sortArr(target):
    change = []
    for r in target:
        dict = defaultdict(int)
        for e in r:
            if e == 0:
                continue
            dict[e] += 1
        tmp = list(dict.items())
        tmp.sort(key = lambda x: (x[1],x[0]))
        a = []
        for i in tmp:
            for j in i:
                a.append(j)
        change.append(a)
    # 행 중에서 가장 크기가 큰 행을 기준으로 빈 칸에는 0을 채운다.
    maxLength = 0
    for i in change:
        maxLength = max(maxLength,len(i))
    for i in change:
        if len(i) < maxLength:
            for _ in range(maxLength-len(i)):
                i.append(0)
    return change 


while True:
    # 정렬이 진행되는 중에 index out of range 에러를 대비하기 위한 조건문.
    if r <= len(arr) and c <= len(arr[0]):
        if arr[r-1][c-1] == k:
            print(t)
            break
        if t > 100:
            if arr[r-1][c-1] != k:
                print(-1)
                break
    # 100 초가 지나고, 정렬을 계속 진행하는 중이라면, break. 위의 조건문에 만족 못하는 경우 대비.
    if t > 100:
        print(-1)
        break
    row= len(arr)
    col = len(arr[0])

    if row >= col:# 행 정렬
        arr = sortArr(arr)
    else: # 열 기준 정렬 (회전하여 행을 기준으로 정렬을 하고 다시 회전 시키기)
        # 90도 오른쪽 회전
        a = []
        for j in range(col):
            tmp = []
            for i in range(row):
                tmp.append(arr[i][j])
            a.append(tmp)
        
        a = sortArr(a)
        
        # 90도 왼쪽으로 회전
        b = []
        for j in range(len(a[0])):
            tmp = []
            for i in range(len(a)):
                tmp.append(a[i][j])
            b.append(tmp)
        arr = b
        
    
    if len(arr) > 100 or len(arr[0]) > 100: # 행 또는 열이 100을 넘어갈때. 첫 100번째까지 자른다.
        cut = []
        for i in range(min(100,len(arr))):
            tmp = []
            for j in range(min(100,len(arr[0]))):
                tmp.append(arr[i][j])
            cut.append(tmp)
        arr = cut
    # 초가 지남.
    t += 1

    ## 알면 좋은 라이브러리: zip(*A) -> 행과 열을 바꿔준다. a = list(zip(*A))
    ## while 문이 종료가 안될 수 있으니 꼭 유심히 조건을 생각해야한다. 또는 for문으로 예방할 수 있다.
