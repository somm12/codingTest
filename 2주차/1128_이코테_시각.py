n = int(input())
h = 0
m = 0
s = 0
cnt = 0

while True:
    if h == n and m == 59 and s == 59:
        print(cnt)
        break
    if '3' in list(str(h) + str(m) + str(s)):
        cnt += 1
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1

# for문을 이용한 방법.
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1