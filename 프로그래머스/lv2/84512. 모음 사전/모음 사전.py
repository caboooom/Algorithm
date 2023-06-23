def solution(word):
    lst = []
    mydict = "AEIOU"
    def makeword(cnt=0, w=""):
        if cnt == 5:
            return lst
        for i in range(len(mydict)):
            lst.append(w+mydict[i])
            makeword(cnt+1, w+mydict[i])
        return lst
    makeword()
    return lst.index(word)+1