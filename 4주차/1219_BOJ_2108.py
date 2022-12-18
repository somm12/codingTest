from collections import Counter
import sys
input = sys.stdin.readline
# 최빈값 배열을 반환.
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/n))
print(arr[n//2])
li = modefinder(arr)
li.sort()
if len(li) > 1:
    print(li[1])
else:
    print(li[0])
print(arr[-1]-arr[0])

# 최빈값은 counter를 사용하여 구할 수도 있다.