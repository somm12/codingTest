def calc(lion,apeach):# 점수 차이 구하기.
    l = 0
    a = 0
    for i in range(11):
        if lion[i] > apeach[i]:
            l += (10-i)
        elif lion[i] < apeach[i]:
            a += (10-i)
        elif lion[i] == apeach[i] and lion[i] != 0:
            a += (10-i)
    return l-a

def solution(n,info):
    cand = []# [[점수차, 라이언의 점수 배열]]
    def dfs(res,L):
        if sum(res) > n: # 만약 합이 n을 넘으면 return
            return
        
        if sum(res) == n or L > 10:# 깊이가 11이 되거나, 합이 n 이 되면 점수차 구하기.
            length = len(res)
            diff = calc(res+ (11-length)*[0], info)
            if diff > 0:# 라이언 점수가 더 크다면, 후보배열에 추가.
                tmp = [diff]+res+ (11-length)*[0] # 이미 n개가 만족 된 경우, 나머지 인덱스에 대해서 0으로 채우기. 
                cand.append(tmp)
            return
        # 0 아니면 어피치 점수의 +1 
        dfs(res+[info[L] + 1], L+1)
        dfs(res+[0], L+1)
    
    dfs([],0)
    
    if len(cand) == 0:# 라이언이 무조건 지거나 비긴다면,
        return [-1]
    # 점수차이, 낮은 점수가 많은 순으로 정렬.
    cand.sort(key=lambda x: (-x[0],-x[11],-x[10],-x[9],-x[8],-x[7],-x[6],-x[5],-x[4],-x[3],-x[2],-x[1]))
  
    tmp = cand[0][1:]
    if sum(tmp) < n:# sum이 n보다 작은 경우가 있을 수 있기 때문에, 0점 부분에 나머지 n-sum(tmp)
        tmp[-1] = n-sum(tmp)
    return tmp
# idx가 11인데 sum(lion) < n인 경우는 라이언이 남은 화살을 모두 과녁의 0점 배점인 곳에 맞혔다고 보면 된다.