s = input()
target = input()
stack  =[]
for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len(target):])==target:# 뒤에서 target 길이 만큼의 문자열과 비교하여 같으면 pop하기.
        for _ in range(len(target)):
            stack.pop()

s = ''.join(stack)

if len(s) == 0:
    print('FRULA')
else:
    print(s)