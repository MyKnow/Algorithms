// [func(Int, Int) -> Int] getGCD: 두 자연수를 입력 받아 최대 공약수를 출력하는 함수
func getGCD(_ a: Int, _ b: Int) -> Int {
    if (b == 0) {
        return a
    } else {
        return getGCD(b, a % b)
    }
}

// [func(Int, Int) -> Int] getLCM: 두 자연수를 입력 받아 최소 공배수를 출력하는 함수
func getLCM(_ a: Int, _ b: Int) -> Int {
    return (a*b) / getGCD(a, b)
}

// [Int] A, B (immutable): 최소 공배수를 계산할 두 자연수(범위(자연수): < 100,000,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (A, B): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// getLCM 함수의 반환 값을 출력
print(getLCM(A, B))