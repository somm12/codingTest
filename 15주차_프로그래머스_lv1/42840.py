def solution(answers):
    answer = []
    ans = []
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    f_cnt = 0
    s_cnt = 0
    t_cnt = 0
    for i in range(len(answers)):
        if f[i%len(f)] == answers[i]:
            f_cnt += 1
        if s[i%len(s)] == answers[i]:
            s_cnt += 1
        if t[i%len(t)] == answers[i]:
            t_cnt += 1
    answer = [f_cnt,s_cnt,t_cnt]
    for i in range(3):
        if answer[i] == max(answer):
            ans.append(i+1)
    
    return ans
#모의고사