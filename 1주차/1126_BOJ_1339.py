n = int(input())
dic = {}
num = []
for _ in range(n):
    arr = list(input())
    for i in range(len(arr)):
        a = len(arr) - i - 1
        if arr[i] not in dic:
            dic[arr[i]] = 10 ** a
        else:
            dic[arr[i]] += 10 ** a

for i in dic.values():
    num.append(i)
num.sort(reverse=True)

res = 0
temp = 9
for v in num:
    res += (temp * v)
    temp -= 1
print(res)
