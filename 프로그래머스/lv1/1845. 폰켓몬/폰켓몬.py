

def solution(nums):
    temp = []
    for i in nums:
        if i not in temp:
            temp.append(i)
        if len(temp) == len(nums)//2:
            break
    return min(len(temp), len(nums)//2)