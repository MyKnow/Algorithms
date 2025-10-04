# 3번의 기회(0~10점)
# S, D, T: 점수 제곱 보너스
# *, #: 이전과 현재 점수 2배(첫번째에서 나올 경우 현재만), 현재 점수 마이너스
# *과 #은 중첩될 수 있으며, 이 경우 아차상의 점수는 -2배가 된다.
# *과 *은 서로 중첩 가능하다.

# format: ns, nd, nt, ns*, nd*, nt*, ns#, ...

import re

def solution(dartResult):
    # 점수, 보너스, 옵션 추출
    pattern = re.compile(r"(\d{1,2})([SDT])([*#]?)")
    matches = pattern.findall(dartResult)

    scores = []

    for i, (point, bonus, option) in enumerate(matches):
        point = int(point)

        # 보너스 적용
        if bonus == 'S':
            point **= 1
        elif bonus == 'D':
            point **= 2
        elif bonus == 'T':
            point **= 3

        # 옵션 적용
        if option == '*':
            point *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif option == '#':
            point *= -1

        scores.append(point)

    return sum(scores)
