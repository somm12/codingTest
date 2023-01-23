s = list(input())
s.sort()
res = 0
alp = ''
for c in s:
    if c.isdigit():
        res += int(c)
    else:
        alp += c

print(alp + str(res))
