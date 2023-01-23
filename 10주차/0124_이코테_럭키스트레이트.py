n = list(map(int, input()))
length = len(n)
left = sum(n[:length//2])
right = sum(n) - left
if left == right:
    print("LUCKY")
else:
    print("READY")
