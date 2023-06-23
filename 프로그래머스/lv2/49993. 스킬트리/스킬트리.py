def solution(skill, skill_trees):
    answer = 0
    # 선행스킬 목록에 있는 스킬은 꼭 모두 순서대로 사용해야함
    
    for lst in skill_trees:
        idx = 0
        flag = True
        for i in lst:
            if i in skill:
                if skill[idx] != i:
                    flag = False
                    break
                idx += 1
        if flag:
            answer += 1
                
    return answer

