n, k = map(int, input().split())
s = list(map(int,input().split()))
s.sort(reverse=True)
print(s[k-1])