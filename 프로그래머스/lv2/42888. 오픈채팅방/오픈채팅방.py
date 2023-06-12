def solution(record):
    answer = []
    user = dict()
    msg = []
    for rec in record:
        temp = rec.split()
        if temp[0] == "Leave":
            msg.append(temp[1]+"님이 나갔습니다.")
            continue
        elif temp[0] == "Enter":
            msg.append(temp[1]+"님이 들어왔습니다.")
        user[temp[1]] = temp[2]
        
    for m in msg:
        uid = m.split()[0][:-2]
        answer.append(m.replace(uid,user[uid]))
    return answer