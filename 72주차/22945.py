n = int(input())
arr = list(map(int,input().split()))

l = 0
r = n-1
answer = 0


# l를 1더하거나 r를 1 빼도 사이에 존재하는 개발자 수는 똑같다
# 그렇다면, min값을 늘려야하기 때문에 더 작은 값을 당겨준다.
while l+1<r:
    value = (r-l-1)*min(arr[l],arr[r])
    answer = max(answer, value)

    if arr[l] < arr[r]:
        l += 1
    else:
        r -= 1
print(answer)

    