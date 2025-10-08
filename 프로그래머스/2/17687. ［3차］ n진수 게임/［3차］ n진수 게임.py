# * 요약
# - n진법을 한 단어씩 끊어서 하나씩 나열 할 때 m 인원 중 p번째 인원인 튜브가 말하는 단어들을 t개 출력해야 한다.

# * 입력
# - n: 진법 (2 ≦ n ≦ 16)
# - t: 튜브가 미리 구할 숫자의 갯수 (1 ≦ t ≦ 1000)
# - m: 게임에 참가하는 인원 (2 ≦ m ≦ 100)
# - p: 튜브의 순서 (1 ≦ p ≦ m)

# * 출력
# - t개를 공백없이 나타낸 문자열
#   - 이 때 10~15는 각각 대문자 A~F로 출력

# * 고찰
# - 시간 제한에 걸리지 않을 것으로 예상되므로 최적화 기법 없이 진행해보자.

# 설계
# 1. 숫자를 외칠 순번인 num(=0)과 모두가 외친 n진법 숫자를 저장할 answer(=[])를 선언한다.
# 2. answer가 m*t 길이가 될 때까지 반복한다.
#   2-1. num을 n진수로 변환하여 answer에 추가한다. (get_base_string_from_number)
#   2-2. num을 1 증가시킨다.
# 3. answer 중에서 규칙과 일치하는 숫자만 리스트로서 반환한다.
#   3-1. [p-1::m]: 튜브가 외친 숫자
#   3-2. [:t]: t개만 추출한다.

# 1. 16진수 문자를 모두 저장한 digits을 선언한다.
# 2. num이 0인 경우를 예외처리 한다.
# 3. num이 0이하가 될 때까지 반복한다.
#   3-1. num을 base로 나눈 몫을 num, 나머지를 rem에 저장한다.
#   3-2. digits의 index에 rem을 활용하여 num을 base진수로 변환하여 res에 추가한다.
# 4. res를 뒤집고 문자열로 변환하여 반환한다.
def get_base_string_from_number(num, base):
    # 1
    digits = "0123456789ABCDEF"
    
    # 2
    if num == 0:
        return "0"
    
    # 3
    res = []
    while num > 0:
        # 3-1
        num, rem = divmod(num, base)
        
        # 3-2
        res.append(digits[rem])
        
    # 4
    return ''.join(reversed(res))

def solution(n, t, m, p):
    # 1
    num = 0
    answer = []
    
    # 2
    while len(answer) < m * t:
        # 2-1
        answer.extend(get_base_string_from_number(num, n))
        
        # 2-2
        num += 1
        
    # 3
    return ''.join(answer[p-1::m][:t])