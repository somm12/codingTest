target = int(input())
m,n = map(int,input().split())
PA = [0]*2001 # 원형 구조를 연속적으로 덧셈을 하려면, 옆에 이어서 붙이는 형식 이므로 최대 길이가 2000 됨.
PB = [0]*2001
ACnt = {}
BCnt = {}
ACnt[target] = 0
BCnt[target] = 0

A= []
B= []
for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))
# A피자 누적합
for i in range(1,m+1):
    PA[i] = PA[i-1]+A[i-1]
for i in range(m+1,(2*m + 1)):
    PA[i] = PA[i-1] + A[i-1 - m]
    
# B피자 누적합.
for i in range(1,n+1):
    PB[i] = PB[i-1]+B[i-1]
for i in range(n+1,2*n + 1):
    PB[i] = PB[i-1] + B[i-1 - n]
# 구간합을 통해서 연속 길이에 따라 나올 수 있는 합의 개수 구하기.
def go(length, PS,dict):
    
    for interval in range(1,length+1):
        for start in range(interval, length + interval):
            total = PS[start] - PS[start-interval]
    
            if total in dict:
                dict[total] += 1
            else:
                dict[total] = 1
            if interval == length:
                break
go(m,PA,ACnt)
go(n,PB,BCnt)
# 각 종류일 때만 경우
answer = ACnt[target] + BCnt[target]
# 혼합하는 경우.
for i in range(1,target):
    if i in ACnt and target-i in BCnt:
        answer += (ACnt[i] * BCnt[target-i])
print(answer)
# 백준 피자판매
# 연속적으로 합 => 누적합 구하기
# 모든 경우의 합을 통해 target만들기 -> 구간합.