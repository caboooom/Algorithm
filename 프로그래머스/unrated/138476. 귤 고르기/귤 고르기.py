from collections import Counter
def solution(k, tangerine):
    answer = 0

    cnt = sorted(Counter(tangerine).values(),reverse = True)

    
    count = 0
    for x in cnt:
        answer += 1
        count += x
        if count >= k:
            return answer