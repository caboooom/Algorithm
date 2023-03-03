def solution(spell, dic):
    for word in dic:
        exist=True
        for s in spell:
            if s not in word:
                exist=False
                break
        if exist==True and len(word)==len(spell):
            return 1
    return 2