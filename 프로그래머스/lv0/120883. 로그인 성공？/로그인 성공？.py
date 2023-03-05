def solution(id_pw, db):
    answer = ''
    for myId, myPw in db:
        if id_pw[0] == myId:
            if id_pw[1] == myPw:
                return "login"
            else:
                return "wrong pw"
    return "fail"