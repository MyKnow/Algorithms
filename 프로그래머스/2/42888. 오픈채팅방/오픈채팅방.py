def solution(record):
    answer = []
    
    user = dict()
    logs = list()
    for log in record:
        splitedLog = log.split(" ")
        
        if len(splitedLog) == 2:
            state, uid = splitedLog
        else:
            state, uid, nickname = log.split(" ")
            user[uid] = nickname
        logs.append([state, uid])
    
    for state, uid in logs:
        if state == "Enter":
            answer.append(user[uid]+"님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(user[uid]+"님이 나갔습니다.")
                    
    return answer