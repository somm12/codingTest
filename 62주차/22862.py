n,k = map(int,input().split())
arr = list(map(int,input().split()))
even = 0
odd = 0
l = 0
r = 0
answer = 0
while r < n:
    if odd > k:# 홀수가 k개 넘어가는 순간. l를 증가시켜서, 범위를 좁힌다.
        if arr[l] %2 == 0:
            even -= 1
        else:
            odd -= 1
        l +=1
    else:# 홀수가 k개 이하라면 r을 증가시킨다.
        if arr[r]%2 == 0:
            even +=1
        else:
            odd +=1
        r  +=1
    answer = max(answer,even)# 짝수 개수 업데이트.
    
print(answer)