a = int(input())
t = int(input())
x = int(input())

bundegi = []
bun = degi = 1
n = 0

while True:
    prev_n = bun
    n += 1
    for _ in range(2):
        bundegi.append((bun, 0))# 몇번째 뻔인지 저장.
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(n+1):
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(n+1):
        bundegi.append((degi, 1))
        degi += 1
    if prev_n <= t <= bun:# index 메소드를 통해서 t번째 뻔 or 데기를 찾고 몇번째 사람인지 출력.
        print(bundegi.index((t, x)) % a)
        break