s = input()
arr = ['pi','ka','chu']
flag= False
i = 0
while i < len(s):# 3가지 중에 찾으면 이동하기. 하지만 없다면 다른 문자열이 있다는 것이므로 break.
    if i < len(s)-1 and (s[i:i+2] == 'pi' or s[i:i+2] == 'ka'):
        i += 2
    elif i < len(s)-2 and s[i:i+3] == 'chu':
        i += 3
    else:
        flag = True 
        break
if flag:
    print("NO")
else:
    print("YES")
# 백준 피카츄.