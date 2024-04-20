# 회전초밥 문제
from collections import defaultdict
import sys
input = sys.stdin.readline
N,d,k,c = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr += arr[:k-1] # 벨트 이기 때문에 마지막 원소 + 처음 K-1개 원소 까지는 확인해야함.
answer = 0
dict = defaultdict(int)

for i in range(k):
    dict[arr[i]] += 1
dict[c] =1
l = 0
r = k-1
while True:

    answer = max(answer,len(dict))

    r+= 1
    if r >= len(arr):
        break
    dict[arr[r]] += 1
    dict[arr[l]] -= 1
    if dict[arr[l]] <= 0:
        del dict[arr[l]]
    l += 1
   
print(answer)

# 다른 풀이
import sys
input = sys.stdin.readline
N,d,k,c = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr += arr[:k-1] # 벨트 이기 때문에 마지막 원소 + 처음 K-1개 원소 까지는 확인해야함.

cnt = [0]*(d+1)# 각 초밥 종류 개수 세는 배열
cnt[c] = 1 # 미리
kind = 1
for i in range(k):
    if cnt[arr[i]] == 0:
        kind+= 1
    cnt[arr[i]] += 1

answer = kind

for i in range(N-1):# 마지막 k개원소 종류를 구할 때는, n-1번째 원소일 때, 오른쪽 추가,i 번째 삭제해서 구하므로, n-1까지.
    if cnt[arr[i+k]] == 0:
        kind += 1
    cnt[arr[i+k]] += 1

    cnt[arr[i]] -= 1
    if cnt[arr[i]] == 0:
        kind -= 1
    
    answer = max(answer,kind)
print(answer)