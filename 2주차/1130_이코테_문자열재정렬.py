arr = list(input())
alpha = []
total = 0
for v in arr:
    if v.isdigit():
        total += int(v)
    else:
        alpha.append(v)
alpha.sort()
ans = ''.join(alpha)

if total != 0:
    ans += str(total)
print(ans)

# join => 리스트를 문자열로 변환하여 출력.
# *예외
# 숫자가 없을 때의 경우도 고려해야함.