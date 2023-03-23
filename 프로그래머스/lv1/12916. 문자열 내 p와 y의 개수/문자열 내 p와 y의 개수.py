from collections import Counter
def solution(s):
    s = s.upper()
    cnt = Counter(s)
    
    if cnt["P"] == cnt["Y"]:
        return True
    return False