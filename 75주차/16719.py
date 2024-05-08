s = input()
n = len(s)
visited = [0]* n
tmp = []
stack = []
for v in s:
    tmp.append(ord(v))
cnt = n

def printResult():
    total = ''
    for i in range(n):
        if visited[i]:
            total += s[i]
    print(total)

while cnt > 0:
    if not stack:
        nxt = 1000
        idx = 0
        for i in range(n):
            if not visited[i] and nxt > tmp[i]:# 제일 앞에꺼. 찾기.
                nxt = tmp[i]
                idx= i
        visited[idx] = 1
        stack.append((nxt,idx))
        cnt -= 1
        printResult() # 출력.
    else:
        isExist = False
        value,idx = stack[-1]
        nxt=1000
        i1 = 0
        for i in range(idx+1,n):# 이전에 사용한 알파벳 이후의 사용 안한 문자들 중 가장 사전 순이 빠른 문자 선택.
            if not visited[i] and nxt > tmp[i]:
                nxt = tmp[i]
                i1 = i
                isExist = True
        if isExist:# 문자가 존재하면 해당 문자 선택.
            visited[i1] = 1
            stack.append((nxt,i1))
            cnt -= 1
            printResult()# 출력.
        else:# 없으면 stack에서 pop
            stack.pop()
# 백준 ZOAC
