def solution(files):
    answer = []
    
    # 1. 파일명을 head, number, tail 로 나누기
    newfiles = []
    original = 0
    for file in files:
        n = len(file)
        idx1 = n
        idx2 = n
        for i in range(n):
            if file[i].isdigit():
                idx1 = min(idx1, i)
            if i > idx1 and file[i].isdigit()==False:
                idx2 = i
                break
        newfiles.append([file[:idx1].lower(),int(file[idx1:idx2]),original])
        #### tail의 내용은 중요하지 않아서 files에서의 인덱스를 저장함
        original += 1
    
    # 2. 정렬
    newfiles.sort(key = lambda x: (x[0], x[1], x[2]))
    
    for file in newfiles:
        answer.append(files[file[2]])
    return answer