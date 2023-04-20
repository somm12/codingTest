answer = int(1e9)
def dfs(total,p_count,m_index,minerals,picks,fatigue):
    global answer
    #광물 다 캤거나 곡쾡이를 다 썼을때 종료
    
    if total == p_count or len(minerals) <= m_index:
        print(fatigue)
        answer = min(answer,fatigue)
        return
    for i in range(len(picks)):
        if picks[i] > 0:
            picks[i] -= 1
            tmp = 0 # 피로도 계산을 합칠 변수
            index = 0# 다음으로 캘 광물 배열의 인덱스를 저장할 변수
            for j in range(m_index,m_index+5):
                index = j
                if j == len(minerals):# 중간에 광물을 다 캐버렸을 경우.
                    break
                    
                if i == 0:# 다이아 곡쾡이일때
                    tmp += 1
                    
                elif i == 1:
                    if minerals[j] == 'diamond':
                        tmp += 5
                    else:
                        tmp += 1
                elif i == 2:
                    if minerals[j] == 'diamond':
                        tmp += 25
                    elif minerals[j] == 'iron':
                        tmp += 5
                    else:
                        tmp += 1
                
            dfs(total,p_count+1,index+1,minerals,picks,fatigue+tmp)
            picks[i] += 1
def solution(picks, minerals):
    total = sum(picks)
    dfs(total,0,0,minerals,picks,0)
    return answer