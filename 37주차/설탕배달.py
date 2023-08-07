n = int(input())
cnt = 0
while n>=0:
    if n % 5 == 0:
        cnt += (n//5)
        print(cnt)
        break
    else:
        n -= 3
        cnt += 1
else:
    print(-1)
# 그리디 설탕배달 복습