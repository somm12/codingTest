n = int(input())
q = [i for i in range(1,n+1)]
step = 1
while q:
    x = q.pop(0)
    if step % 2 != 0:
        print(x,end= ' ')
    else:
        q.append(x)
    step += 1