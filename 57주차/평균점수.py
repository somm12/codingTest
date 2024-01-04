answer = 0
for _ in range(5):
    a = int(input())
    if a < 40:# 40점 미만은 40점.
        answer += 40
    else:
        answer += a
print(answer//5)