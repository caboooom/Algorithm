def solution(cipher, code):
    answer = ''
    idx=code-1
    for i in range(len(cipher)//code):
        answer += cipher[idx]
        idx += code
    return answer