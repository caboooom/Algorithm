def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in skip:
        alphabet = alphabet.replace(x,'')
    for x in s:
        idx = alphabet.index(x)
        answer += alphabet[(idx+index)%len(alphabet)]
    return answer