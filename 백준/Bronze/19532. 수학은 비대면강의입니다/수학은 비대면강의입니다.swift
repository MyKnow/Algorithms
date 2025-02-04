// [Int] a, b, c, d, e, f (immutable): 연립방정식의 계수 (범위(정수): -999 <= ... <= 999)
let arrayOfInput: Array<Int> = (readLine() ?? "0 0 0 0 0 0").split(separator: " ").compactMap { Int($0) }
let (a, b, c, d, e, f): (Int, Int, Int, Int, Int, Int) = (arrayOfInput[0], arrayOfInput[1], arrayOfInput[2], arrayOfInput[3], arrayOfInput[4], arrayOfInput[5])
    
// [Bool] isFound (mutable): 찾았는 지 여부 체크 (초기값: false)
var isFound: Bool = false

for x in -999...999 {
    for y in -999...999 {
        if ((a * x + b * y == c) && (d * x + e * y == f)){
            print(x, y)
            isFound = true
            break
        }
    }
    if (isFound) {
        break
    }
}