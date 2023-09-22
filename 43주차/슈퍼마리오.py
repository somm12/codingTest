arr = []
total = 0
for _ in range(10):
    a = int(input())
    total += a
    arr.append((abs(100-total),total))
arr.sort()
if arr[0][0] == arr[1][0]:
    print(max(arr[0][1],arr[1][1]))
else:
    print(arr[0][1])
# 백준 문제. 숫자들의 합이 100과 가장 가까울 때의 점수구하기.