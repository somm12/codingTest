s = input()
a = input()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    
    if ''.join(stack[-len(a):]) == a:
        for _ in range(len(a)):
            stack.pop()

s = ''.join(stack)
if len(s) == 0:
    print('FRULA')
else:
    print(s)
# 스택을 이용해서 문자열 비교를 통해 a와 같아지면 그만큼 pop
# 100만 * 72번.