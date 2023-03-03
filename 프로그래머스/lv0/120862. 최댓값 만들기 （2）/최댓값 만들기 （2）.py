def solution(numbers):
    
    numbers.sort()
    if len(numbers)>=3:
        return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
        
    return numbers[0]*numbers[1]
   