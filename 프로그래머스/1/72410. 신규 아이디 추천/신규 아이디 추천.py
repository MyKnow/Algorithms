# 아이디 규칙 -> new_id
# 1. 3자 이상 15자 이하
# 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
# 3. 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없다.


# 7단계에 거쳐 ID Validation을 진행해야 한다.
# 우선 길이 관련된 처리를 진행하여 시간복잡도를 최소화 해야 한다.
def solution(new_id):
    answer = ''
    allowed_char_set = set(["-", "_", "."])
        
    # 1. 대문자를 대응하는 소문자로 치환한다.
    new_id = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자를 제거한다.
    # 알파벳, 숫자가 아니거나, allowed_char_set에 포함되지 않은 문자는 제거한다.
    tmp = ""
    for char in new_id:
        if char.isalpha() or char.isnumeric() or (char in allowed_char_set):
            tmp += char
    new_id = tmp
            
    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환한다.
    tmp = ""
    flag = False
    for char in new_id:
        if char == ".":
            if flag:
                continue
            else:
                flag = True
                
        else:
            flag = False
        
        tmp += char
    new_id = tmp
    
    # 4. 마침표가 처음 또는 끝에 위치한다면 제거한다.
    if new_id[0] == ".":
        new_id = new_id[1:]
        
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
            
    print(new_id)
    # 5. 아이디가 빈 문자열이라면 "a"로 바꾼다.
    if len(new_id) == 0:
        new_id = "a"
        
    # 6. 아이디 길이가 16자 이상이면, 처음 15자를 제외한 나머지 문자들을 제거한다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    # 7. 아이디 길이가 2자 이하라면, 마지막 문자를 길이 3까지 반복해서 끝에 붙인다.
    if len(new_id) <= 2:
        last_word = new_id[-1]
        new_id += last_word * (3-len(new_id))
        
        
    
    # 4. 마침표가 처음 또는 끝에 위치한다면 제거한다.
    if new_id[0] == ".":
        new_id = new_id[1:]
        
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    return new_id