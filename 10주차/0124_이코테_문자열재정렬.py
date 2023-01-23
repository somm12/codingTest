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

# 다른 풀이. ** sort는 배열만 가능, join을 통해 배열을 문자열로 변환 가능
data = input()
result = []# 문자를 담을 배열
value = 0# 각 숫자를 더할 변수

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))