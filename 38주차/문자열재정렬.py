s = input()
alpha = []
num = []
for v in s:
    if v.isdecimal():
        num.append(v)
    else:
        alpha.append(v)
    
alpha.sort()
num= list(map(int,num))

answer = ''
for v in alpha:
    answer+= v
total = sum(num)

answer += str(total)
print(answer)