def solution(numbers):
    answer = []
    
    for i in numbers:
        if i%2 == 0:
            answer.append(i+1)
        else:
            add = []
            for j in bin(i)[::-1]:
                if j == "0" or j=="b":
                    add.append("1")
                    break
                add.append("0")
            result = ''.join(reversed(add))
            k = int(result,2)
            answer.append(int(i) + k - k//2)
    return answer