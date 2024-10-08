import math
n,L = map(int,input().split())
cnt = 0
answer = 0
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b-1])

arr.sort()

pos=0
for s,e in arr:
    
    if pos < s:#웅덩이가 판지 보다 멀리 있는 경우
        cnt = math.ceil((e-s+1)/L)
        answer += cnt
        pos = s + (cnt*L) - 1
    elif s <= pos < e:# 판지가 현재 웅덩이 사이에 위치한다면
        cnt = math.ceil((e-pos)/L)
        pos = pos + L*cnt
        
        answer += cnt
    else:# 판지가 현재 웅덩이를 포함하는 경우.
        continue
print(answer)
#백준 1911.