n = int(input())
J,S = n,n # 준현, 성민이 가진 돈

JCnt, SCnt = 0,0 # 준혁, 성민 주식 개수
arr = list(map(int,input().split()))

# 준현이 주식 계산
for v in arr:
    if J >=v:
        JCnt += (J//v)
        J %= v
# 성민이 주식 계산
for i in range(3,len(arr)):
    if arr[i-3] < arr[i-2] < arr[i-1]: # 3일 연속 상승 => 전매도
        S += (SCnt*arr[i])
        SCnt = 0
    if S >= arr[i] and arr[i-3] > arr[i-2] > arr[i-1]: # 3일 연속 하락 => 전매수
        SCnt += (S//arr[i])
        S %= arr[i]

    

a = J+(arr[-1]*JCnt)
b = S +(arr[-1]*SCnt)
if a >b:
    print("BNP")
if a <b:
    print("TIMING")
if a == b:
    print("SAMESAME")
# 백준 구현 기적의 매매법.