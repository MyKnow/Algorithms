// [Dictionary<String, Float>] gradeTable (immutable): (등급, 점수)로 이루어진 Dictionary
let gradeTable: Dictionary<String, Float> = [
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0,
]

// [Float] totalGradePoint (mutable) : 학점 x 과목평점의 합
var totalGradePoint: Float = 0.0

// [Float] credit (mutable) : 총 이수 학점
var credit: Float = 0.0

// 한 줄씩 읽고 처리
while let line = readLine() {
    // 개행 문자 제거
    // line = line.trimmingCharacters()
    
    // [Array<String>] arrayOfLecture (immutable) : 강의의 이름, 학점, 평점으로 이루어진 배열 (길이: 3)
    let arrayOfLecture: Array<String> = String(line).split(separator: " ").map {String($0)}
    
    // [Float] point : 해당 과목의 이수 학점
    let point: Float = Float(arrayOfLecture[1]) ?? 0.0
    
    // [String] grade : 해당 과목의 평점
    let grade: String = arrayOfLecture[2]
    
    // 만약 평점이 P라면 계산하지 않는다.
    if (grade == "P") {
        continue
    }
    
    // 이수 학점에 해당 강의의 학점을 더한다.
    credit += point
    
    // totalGradePoint에 학점 x 과목 평점을 더한다.
    totalGradePoint += point * Float((gradeTable[grade]) ?? 0.0)
}
    
// totalGradePoint을 credit으로 나눈 GPA를 출력한다.
print(totalGradePoint/credit)