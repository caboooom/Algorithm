def solution(str1, str2):
    answer = 0
    
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()
    
    set1 = dict()
    set2 = dict()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            if str1[i:i+2] not in set1:
                set1[str1[i:i+2]] = 1
            else:
                set1[str1[i:i+2]] += 1
                
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            if str2[i:i+2] not in set2:
                set2[str2[i:i+2]] = 1
            else:
                set2[str2[i:i+2]] += 1

    inter = set(set1).intersection(set(set2))
    uni = set(set1).union(set(set2))
    
    sum1 = 0
    sum2 = 0
    for i in inter:
        sum1 += min(set1[i], set2[i])
        sum2 += max(set1[i], set2[i])
    
    for i in uni:
        if i not in inter:
            if i in set1:
                sum2 += set1[i]
            else:
                sum2 += set2[i]
                
    if sum2 > 0:
        return int(sum1/sum2 * 65536)
    return 65536