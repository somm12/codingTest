a = input().split('-')
answer = 0
for i in a[0].split('+'):
    answer += int(i)
for v in a[1:]:
    for j in v.split('+'):
        answer -= int(j)
print(answer)
'''split를 이용하는 것이 핵심.'''