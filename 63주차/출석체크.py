import sys
input = sys.stdin.readline
n,k,Q,M = map(int,input().split())
arr = [1]*(n+3)
for i in range(3):
    arr[i] = 0

sleeping = list(map(int,input().split()))# 자는 학생번호.
student= list(map(int,input().split()))

for v in sleeping:
    arr[v] = 1 # 자는 학생은 출석 체크 안함.
sleeping = set(sleeping)

for num in student:
    if num not in sleeping:# 자는 학생이 아니라면, 배수인 학생들에게 출석 코드 보냄.
        for i in range(1,n+3):
            if num*i > n+2:
                break
            if num*i not in sleeping:# 배수 자체가 자는 애가 아니면 출석.
                arr[num*i] = 0

pSum = [0]*(n+3)
total = 0
for i in range(3,n+3):
    total += arr[i]
    pSum[i] = total

for _ in range(M):
    s,e = map(int,input().split())
    print(pSum[e]-pSum[s-1])
