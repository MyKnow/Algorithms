# * 요약
# - 멜로디 문자열과 곡정보 리스트가 주어지면, 조건이 일치하는 곡의 제목을 반환하라

# * 입력
# - m: 네오가 기억한 멜로디(1개 이상 1,439개 이하)
    # - C, C#, D, D#, E, F, F#, G, G#, A, A#, B (12개)
# - musicinfos: "HH:MM(시작 시간),HH:MM(끝난 시각),음악제목,악보정보" 형태의 문자열 리스트 (100개 이하)
#   - 각 음은 1분에 1개씩 재생됨.
#       - 음악 길이보다 재생된 시간이 길 때는 끊김 없이 처음부터 반복해서 재생됨.
#       - 음악 길이보다 재생된 시간이 짧을 때는 재생 시간만큼만 재생됨.
#       - 00:00을 넘겨서까지 재생되는 일은 없음.
#   - 각 시각: 24시간 형식.
#   - 음악제목: "," 이외의 출력 가능한 문자만 존재 (1 이상 64 이하의 문자열)
#   - 악보정보: 1개 이상 1,439개 이하로 구성

# * 출력
# - 조건에 일치하는 음악 제목 출력
#   - 일치하는 음악이 없을 때에는 (None) 반환
#   - 일치하는 음악이 여러 개일 때에는 재생된 시간이 제일 긴 음악 제목을 반환한다.
#       - 시간이 같을 경우엔 먼저 입력된 음악 제목을 반환한다.

# * 고찰
# 1. 각 시각은 단순히 음악 정보를 조건에 맞춰 가공하기 위해서만 사용될 것이다.
# 2. (1)에 의해 가공된 musicinfos 속 음악정보에, m값이 포함되면 조건에 일치하는 것이다.
# 3. 단순히 str.find로 일치 여부를 확인하기엔 "C#", "D#" 등과 같은 2자리 음이 존재한다.

def getTimeValue(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def trans_melody(s):
    # 검은 건반을 처리하기 위해서 간단히 다른 문자로 바꾸는 방법을 택한다.
    return (s.replace('C#', '1')
             .replace('D#', '2')
             .replace('E#', '3')
             .replace('F#', '4')
             .replace('G#', '5')
             .replace('A#', '6')
             .replace('B#', '7'))

def solution(m, musicinfos):
    # musicinfos를 시작 시간 순으로 정렬한다.
    musicinfos.sort()
    
    # 반음처리
    m = trans_melody(m)
    
    # musicinfos를 순회하며 조건 일치 여부를 확인한다.
    # 조건이 일치할 경우 (재생시간, 이름) 튜플을 저장한다.
    matched = (0, "(None)")
    for info in musicinfos:
        # 구분자인 ","를 통해 분할한다.
        start, end, title, melodies = info.split(",")
        
        # 계산의 편의를 위해, HH:MM 형태의 시각을 정수로 변환한다.
        start, end = getTimeValue(start), getTimeValue(end)
        
        # 반음처리
        melodies = trans_melody(melodies)
        
        # duration: 곡이 재생된 시간 
        duration = end - start
        
        melody_len = len(melodies)
        # 재생시간이 음악시간보다 긴 경우
        if melody_len < duration:
            # 남은 시간만큼 melodies를 반복한다.
            melodies = melodies * (duration // melody_len) + melodies[:duration % melody_len]
        # ~보다 짧은 경우, duration만큼 멜로디를 자른다.
        else:
            melodies = melodies[:duration]
        
        # in을 통해서 동일 멜로디가 존재하는 지 확인한다.
        # 존재한다면 튜플 업데이트를 시도한다.
        if m in melodies:
            # 이 때 이미 tuple에 현재 곡보다 길이가 긴 음악이 존재한다면 무시한다.
            if matched[0] < duration:
                matched = (duration, title)
        
    return matched[1]