// [Array<Int>] listOfAngles: 각도들을 저장하는 배열 (길이: 3)
var listOfAngles: [Int] = []

for _ in 0..<3 {
    listOfAngles.append(Int(readLine() ?? "60") ?? 60)
}

// 세 각의 합이 180이 아닌 경우 에러
if (listOfAngles.reduce(0, +) != 180) {
    print("Error")
}
// 정삼각형 판별 (모든 각이 60도)
else if (listOfAngles.allSatisfy({ $0 == 60 })) {
    print("Equilateral")
}
// 이등변 삼각형 판별 (같은 값이 최소 하나 있는 경우)
else if (Set(listOfAngles).count == 2) {
    print("Isosceles")
}
// 부등변 삼각형 판별 (모든 각이 다 다른 경우)
else {
    print("Scalene")
}