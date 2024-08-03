

answer = 0
n = int(input())
s = input()
stk = [-1]# 스택 역할하는 배열. 한덩어리의 올바른 괄호 길이를 계산하기 위해서 -1 미리 추가.
#  ( ( ) ) 경우일 때, 0 1 2 3 => 닫는 괄호가 나왔을 때 인덱스를 이용해서 길이를 구하는 방법.
for i in range(n):
    if s[i] == '(':# 여는 괄호는 추가.
        stk.append(i)
    else:
        stk.pop()
        if stk:
            answer= max(answer, i - stk[-1])
        else:
            stk.append(i)


print(answer)
# 백준 현욱이는 괄호왕