n,m = map(int,input().split())
answer = 0
s = {}
for _ in range(n):
    tmp = input()
    s[tmp] = 1;

for _ in range(m):
    tmp = input()
    if tmp in s:
        answer += 1

print(answer)
# 코드트리 hashset, string 문제