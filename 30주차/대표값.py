from collections import defaultdict
dict = defaultdict(int)
total = 0
for _ in range(10):
    n = int(input())
    total += n
    dict[n] += 1
dict = list(dict.items())
dict.sort(key=lambda x: (-x[1]))

print(total//10)
print(dict[0][0])
