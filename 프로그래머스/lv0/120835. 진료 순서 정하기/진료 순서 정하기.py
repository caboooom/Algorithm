def solution(emergency):
    arr = sorted(emergency,reverse=True)
    ans=[]
    for i in emergency:
        for j in range(len(arr)):
            if i==arr[j]:
                ans.append(j+1)
    return ans