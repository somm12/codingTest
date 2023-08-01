n = int(input())
answer =0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            h = str(h)
            m = str(m)
            s = str(s)
            if '3' in h+m+s:   
                answer += 1
print(answer)
# 이코테 구현 예제