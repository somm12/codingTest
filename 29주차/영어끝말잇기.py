def solution(n,words):
    answer = [] # 정답을 담을 변수.
    prev = ' ' # 초기 이전 단어를 초기화.
    now = 1 # 현재 몇 차례인지 담는 변수.
    did = {} # 이미 말한 단어를 담는 딕셔너리.
    for i,v in enumerate(words):
        now = (i+1)//n # 현재 몇 차례인지 나타내는 now
        if (i+1) % n > 0:
            now += 1
        # 처음은 넘어가고, 이전에 말했던 것 or 한 글자 단어 or 이전 단어 마지막 글자 != 현재 첫글자.
        if i != 0 and (v in did or len(v) == 1 or prev[-1] != v[0]): # 탈락 조건 만족시,
            if (i+1) % n == 0:
                num = n 
            else:
                num = (i+1) % n # 현재 idx+1 % n => 사람 번호. 단, 나머지가 0이면 번호는 n.
            answer = [num, now] # [사람번호, 현재 차례] 반환.
            return answer
        else:
            did[v] = 1 # 바르게 했을 시, 이미 말한 단어를 dictionary에 추가.
            prev = v # 이전 단어 update.
    return [0,0] # 탈락자가 없다면 [0,0] 반환.

# 프로그래머스 lv2