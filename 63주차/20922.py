n,k = map(int,input().split())
arr = list(map(int,input().split()))

maxV = max(arr)

count = [0]*(maxV+1)

l,r = 0,0
answer = 1
while r < n and l <= r:
    if count[arr[r]] >= k:
        count[arr[l]] -= 1
        l += 1
    else:
        count[arr[r]] += 1
        r+= 1
    answer = max(answer,r-l)
    # K개를 초과하려하면, 범위를 좁혀나가고, 아니면 계속 범위를 늘린다. 이에 따라서 가능한 수열이 변경됨.
    # => 매 반복문 마다 l와r 차이로 길이 update
    
print(answer)