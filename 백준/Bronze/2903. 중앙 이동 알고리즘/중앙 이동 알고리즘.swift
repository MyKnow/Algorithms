// [Int] N (immutable): 중앙 이동 알고리즘을 적용하는 횟수 (범위 : 1 <= N <= 15)
let N: Int = Int(readLine() ?? "1") ?? 1

// 과정을 거듭할 때마다 한 변의 사각형의 개수는 2배씩 늘어남
// 1, 2, 4, 8, ..., 2^n
// [Int] squaresOfSide (mutable): 한 변의 사각형 개수
var squaresOfSide: Int = 1
for _ in 0..<N {
    squaresOfSide *= 2
}

// 한 변을 구성하는 점의 개수는 사각형의 점 개수 + 1
// [Int] pointsOfSide (immutable): 한 변의 점의 개수
let pointsOfSide: Int = squaresOfSide + 1

// 점의 총 개수는  pointsOfSide의 제곱
print(pointsOfSide*pointsOfSide)