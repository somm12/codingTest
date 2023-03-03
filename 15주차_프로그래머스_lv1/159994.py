def solution(cards1, cards2, goal):
    answer = ''
    idx1 = 0
    idx2 = 0
    for i in range(len(goal)):
        if goal[i] == cards1[idx1]:
            if idx1 < len(cards1) - 1:
                idx1 += 1
        elif goal[i] == cards2[idx2]:
            if idx2 < len(cards2) - 1:
                idx2 += 1
        else:
            return 'No'
    return 'Yes'