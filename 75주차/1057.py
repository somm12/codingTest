n,a,b =map(int,input().split())
if a>b:
    a,b=b,a

answer = -1
cnt = 1

while n > 1:
    if a+1 == b and a % 2 == 1:# 순서대로 홀수번호, 짝수번호가 인접하다면 그 때 경기.
        answer = cnt
        break
    a = (a+1)//2
    b = (b+1)//2
    cnt += 1
    n = (n+1)//2
print(answer)
#토너먼트