n = int(input())
cand = []
visited = [0]*10

def init():# 서로 다른 3자리 수 전체 구하기.
    global cand
    def dfs(res):
        if len(res) == 3:
            cand.append(int(res))
            return
        for i in range(1,10):
            if not visited[i]:
                visited[i] = 1
                dfs(res+str(i))
                visited[i] = 0
    dfs('')

init()

def game(tmp):# 입력에 해당하는 결과 인지 체크.
    global num
    num = str(num)
    tmp = str(tmp)
    strike, ball = 0,0
    for i in range(3):
        if num[i] == tmp[i]:
            strike += 1
        elif tmp[i] in num:
            ball += 1
    if [strike, ball] == [s,b]:
        return True
    return False


def check():# 현재 입력에 해당하는 결과에 해당하는 모든 숫자 담기.
    result = []
    for tmp in cand:
        if game(tmp):
            result.append(tmp)
    return result

for _ in range(n):
    num,s,b = map(int,input().split())
    cand = check()# 한 줄 입력씩, 추측 가능한 숫자들을 추려내어 업데이트하기.
   
print(len(cand))# 가능한 숫자 출력.
# 숫자 야구