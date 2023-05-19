import math
n = int(input())
arr = list(map(int,input().split()))
B,C = map(int,input().split())
answer = n # 오직 한 명씩 총감독관이 배치돼야함.
for x in arr:
    x -= B # 총감독관이 감시하는 B명 제외.
    if x > 0: # 0보다 크다면
        if x % C: # 나머지가 있으면 + 1명
            answer += x//C + 1
        else: # 나누어 떨어지면 그대로.
            answer += x//C
print(answer)