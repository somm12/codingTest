import sys
input = sys.stdin.readline
s = input().rstrip()
p = []
v = s[0]
one = 0
zero = 0
for i in range(1, len(s)):
    if s[i] == v[-1]:
        v += s[i]
    else:
        p.append(v)
        if v[0] == '0':
            zero += 1
        else:
            one += 1
        v = s[i]
if v[-1] == '0':
    zero += 1
else:
    one += 1
print(min(one, zero))

# 더 쉬운 방법 ( 0과 1 서로 바뀌는 시점에서 count하기)
if s[0] == '1':
    zero += 1
else:
    one += 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            zero += 1
        else:
            one += 1
print(min(zero,one))
