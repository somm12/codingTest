s = input()
a = ''
for i in s:
    if i.islower():
        a += i.upper()
    else:
        a += i.lower()
print(a)