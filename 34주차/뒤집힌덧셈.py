a,b = map(int,input().split())

def rev(x):
    tmp = list(str(x))
    tmp.reverse()
    tmp = ''.join(tmp)
    return int(tmp)

print(rev(rev(a) + rev(b)))