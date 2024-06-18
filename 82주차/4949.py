arr = set(['(',')','[',']'])

while True:
    s = input()
    if s =='.':
        break
    stack =[]
    for v in s:
        if v not in arr:
            continue
        if not stack:
            stack.append(v)
            
        elif stack[-1] == '(' and v == ')':
            stack.pop()
        elif stack[-1] == '[' and v ==']':
            stack.pop()
        else:
            stack.append(v)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
# 백준 균형잡힌 세상