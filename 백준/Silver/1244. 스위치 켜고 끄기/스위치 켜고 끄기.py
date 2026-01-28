# 1부터 연속적으로 번호가 붙어있는 스위치 (On: 1, Off: 0)
#
# 몇 명의 학생을 뽑아서, 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어 줌
# -> 성별과 받은 수에 따라 스위치를 조작하게 됨
# 남학생: 스위치 번호가 자기가 받은 수의 배수이면 해당 스위치의 상태 reverse
# 여학생: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로,
# 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
# 그 구간에 속한 스위치의 상태를 모두 바꿈.
# 이 때 구간에 속한 스위치 개수는 항상 홀수.

# 첫째 줄에는 스위치 개수(100 이하인 양의 정수)
# 둘째 줄에는 각 스위치의 상태(정수 리스트)
# 셋째 줄에는 학생 수 (100 이하))
# 넷째 줄부터 마지막까지 학생의 성별(남:1, 여:2)과 받은 수(스위치 개수 이하) 쌍

import sys
input = sys.stdin.readline

number_of_switch = int(input())

switches = [-1]
for state in map(int, input().split()):
    switches.append( state == 1 )

number_of_student = int(input())
for _ in range(number_of_student):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number, number_of_switch + 1, number):
            switches[i] = not switches[i]
    else:
        # 1. 범위를 벗어나거나
        # 2. 두 스위치의 상태가 다르면 종료
        range_of_reverse = 0
        for d in range(1, min(number - 1, number_of_switch - number) + 1):
            # 두 스위치 상태가 다르면 break
            if (switches[number-d] != switches[number+d]):
                break
            range_of_reverse = d
                
        # 같으면 reverse
        for i in range(number-range_of_reverse, number+range_of_reverse+1):
            switches[i] = not switches[i]

for i in range(number_of_switch):
    if i != 0 and i % 20 == 0:
        print()
    print(1 if switches[i+1] else 0, end=" ")