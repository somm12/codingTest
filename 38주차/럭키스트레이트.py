n = input()
mid = len(n)//2

left = n[:mid]
right = n[mid:]

l = list(map(int,left))
r = list(map(int, right))

if sum(l) == sum(r):
    answer = 'LUCKY'
else:
    answer = 'READY'
print(answer)
