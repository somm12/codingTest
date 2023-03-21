def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        for s in i:
            if s not in skill:
                i = i.replace(s,'')
        for idx in range(len(i)):
            if i[idx] != skill[idx]:
                break
        else:
            answer += 1

    return answer
# 스킬트리