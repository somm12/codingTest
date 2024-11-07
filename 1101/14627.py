s,c = map(int,input().split())
arr = []
for _ in range(s):
    arr.append(int(input()))
s = 1
e = int(1e9)
answer = 0

def check(mid):
    res = 0
    for v in arr:
        res += (v//mid)
    return res

while s<=e:
    mid = (s+e)//2
    cnt = check(mid)
    if cnt >= c:# 해당 길이 만큼 파를 잘랐을 때, c개의 파닭을 만들 수 있다면, 파 길이 범위를 증가시킴.
        answer = mid
        s = mid +1
    else:
        e = mid - 1
        
result =0

# 문제에서 주문받은 파닭의 길이만큼만 사용해야함. 
# 모듈러 연산을 하게 되면 더 사용하게 되는 경우가 생김.
print(sum(arr) - (c*answer))
# 백준 파닭파닭