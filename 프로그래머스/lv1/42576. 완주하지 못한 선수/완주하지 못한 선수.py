def solution(participant, completion):
    pdict = dict()
    for p in participant:
        if p in pdict:
            pdict[p] += 1
        else:
            pdict[p] = 1
            
    for p in completion:
        pdict[p] -= 1
        
    for x in pdict:
        if pdict[x] > 0:
            return x