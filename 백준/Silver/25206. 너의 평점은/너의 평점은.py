# stdin을 위한 sys import
import sys

# [dict(string, float)] gradeTable : (등급, 점수)로 이루어진 Dictionary
gradeTable = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
}

# [float] totalGradePoint : 학점 x 과목평점의 합
totalGradePoint = 0.0

# [float] credit : 총 이수 학점
credit = 0.0

# 한 줄씩 읽고 처리
for line in sys.stdin:
    # 개행 문자 제거
    line = line.strip()
    
    # [tuple(string, string, string)] tupleOfLecture : 강의의 이름, 학점, 평점으로 이루어진 튜플
    tupleOfLecture = line.split(" ")
    
    # [float] point : 해당 과목의 이수 학점
    point = float(tupleOfLecture[1])
    
    # [string] grade : 해당 과목의 평점
    grade = tupleOfLecture[2]
    
    # 만약 평점이 P라면 계산하지 않는다.
    if (grade == "P"):
        continue
    
    # 이수 학점에 해당 강의의 학점을 더한다.
    credit += point
    
    # totalGradePoint에 학점 x 과목 평점을 더한다.
    totalGradePoint += point * float(gradeTable[grade])
    
# totalGradePoint을 credit으로 나눈 GPA를 출력한다.
print(totalGradePoint/credit)