
n,k = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
count = [0] * (max(arr)+1)
answer = 0
right = 0

while right < n:
    if count[arr[right]] < k:# K개 미만이면 증가시키기.
        count[arr[right]] += 1
        right += 1
    else:
        count[arr[left]] -= 1
        left += 1
    
    answer = max(answer,right-left)
    
print(answer)
# K개이상이라면, left를 증가시켜서 범위를 좁힌다
# -> 그러다 right 와 Left가 가리키는 값이 동일해지면 자동으로 coun값이 줄어들어서 right가 계속해서 범위를 넗혀간다.