import math
n = int(input())
arr = list(map(int,input().split()))

answer = 0
leader, p = map(int,input().split())

answer += n # 최소 가게당 팀장 한명은 배치 되어야함.

for v in arr:
    tmp = v - leader
    if tmp > 0:
        answer += math.ceil(tmp/p) # 팀장이 검사하고 남은 인원이 있다면 팀원이 검사

print(answer)
# 코드트리 문제