n = int(input())
coin = [500, 100, 50, 10, 5, 1]
ans = 0

money = 1000 - n
for c in coin:
    ans += (money // c)
    money = money % c
print(ans)