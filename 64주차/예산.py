n = int(input())
arr =list(map(int,input().split()))

limit = int(input())
s = 1
e = max(arr)

while s <= e:
    mid= (s+e)//2
    total = 0
    for v in arr:
        if v <= mid:
            total += v
        else:
            total += mid
    if limit < total:# 상한액보다 초과한다면 범위 줄이기
        e = mid - 1
    else:# 상한액 이하의 값이 된다면, 범위를 늘리고 가장 예산가 가까워지는 최대 상한액을 저장한다.
        s = mid + 1
        answer = mid

print(answer)