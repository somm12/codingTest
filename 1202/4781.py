while True:
    n,m = input().split()
    n = int(n)
    if n == 0:
        break
    m1,m2 = map(int,m.split("."))
    cost = m1*100 + m2
    dp = [0]*(cost+1)
    
    for _ in range(n):
        c,p = input().split()
        p1,p2 = map(int,p.split("."))
        c = int(c)
        price = p1*100 + p2
        
        
        for i in range(price,cost+1):
            dp[i] = max(dp[i], dp[i-price] + c)# i-price일 때의 최대 + c더하면서 갱신.
    print(dp[cost])

# 백준 사탕가게
# 정수로 바꿔서 계산하기.