def solution(s):
    arr = list(s.split())
    ans = 0
    for i in range(len(arr)):
        if arr[i]=='Z':
            ans -= int(arr[i-1])
        else:
            ans += int(arr[i])
    return ans