import math
def solution(n, words):
    answer = []

    player = 0
    idx = 0
    last = words[0][0]
    wordset = set()
    
    for i in words:
        if i[0] != last or i in wordset:
            break
        wordset.add(i)
        last = i[-1]
        player = (player+1)%n
        idx += 1
        
    if idx == len(words): return [0,0]
    return [player+1, math.ceil((idx+1)/n)]