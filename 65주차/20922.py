n,k = map(int,input().split())
arr = list(map(int,input().split()))
maxV = max(arr)
cnt = [0]*(maxV + 1)
s = 0
e = 0
answer = 0
while s <= e and e < n:
  v = arr[e]
  if cnt[v] < k:# 원소의 개수가 k개 미만이라면, 증가 시키기.
    cnt[v]+= 1# 개수 증가
    e += 1# 포인터 위치 이동
  else:
    cnt[arr[s]] -= 1# 원소 개수가 k개를 넘는다면, 범위 줄이기
    s += 1
  answer = max(answer, e-s)
print(answer)