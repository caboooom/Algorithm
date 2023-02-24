#절단기 높이가 height일 때 잘린 나무의 길이 리턴하는 함수
def cut(arr, height):
  sum = 0
  for i in arr:
    if i>=height:
      sum += i - height
  return sum


def search(arr, target, start, end):
  result = 0
  while start <= end:
    mid = (start+end)//2
    #길이가 남으면, start 위치 조정하고 높이 저장
    if cut(arr,mid) >= target:
      result = mid
      start = mid + 1
    #길이가 부족하면, end 위치 조정
    else:
      end = mid - 1
  return result
  
n,m = map(int,input().split())
arr = list(map(int,input().split()))

print(search(arr, m, 0, max(arr)))
