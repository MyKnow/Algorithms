# students: list - 과제를 제출했는 지 여부를 확인하는 리스트 (길이: 30)
# 기본 값: 0, 과제를 제출한 경우 1로 업데이트 됨.
students = [0] * 30

# 28번 입력을 받음
for _ in range(28):
    # 출석 번호가 1부터 시작하므로, 입력 값-1의 학생을 1로 업데이트 함
    students[int(input())-1] = 1

# 과제를 제출하지 않은 학생을 찾으면 print함
for student in range(1, 31):
    if (students[student - 1] == 0) :
        print(student)