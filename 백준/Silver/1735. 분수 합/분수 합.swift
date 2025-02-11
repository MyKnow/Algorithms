// [func(Int, Int) -> Int] getGCD: 최대 공약수를 반환하는 함수
func getGCD(_ a: Int, _ b: Int) -> Int {
    if (b==0) {
        return a
    }
    else {
        return getGCD(b, a%b)
    }
}

// [func(Int, Int) -> Int] getLCM: 최소 공배수를 반환하는 함수
func getLCM(_ a: Int, _ b: Int) -> Int {
    return (a*b)/getGCD(a, b)
}

// [Int] numerator1, denominator1 (immutable): 첫번째 분자와 분모 (범위(자연수): <= 30,000)
let inputOfFirstFraction: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (numerator1, denominator1): (Int, Int) = (inputOfFirstFraction[0], inputOfFirstFraction[1])

// [Int] numerator2, denominator2 (immutable): 두번째 분자와 분모 (범위(자연수): <= 30,000)
let inputOfSecondFraction: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (numerator2, denominator2): (Int, Int) = (inputOfSecondFraction[0], inputOfSecondFraction[1])

// [Int] dOfReducedFraction (Immutable): 예비 기약분수의 분모, 두 분모의 최소 공배수.
let dOfReducedFraction: Int = getLCM(denominator1, denominator2)

// [Int] nOfReducedFraction (Immutable): 예비 기약분수의 분자, 최소 공배수와 각 분모를 나눈 값을 분자에 곱하여 모두 더한 값
let nOfReducedFraction: Int = ((dOfReducedFraction/denominator1) * numerator1) + ((dOfReducedFraction/denominator2) * numerator2)

// [Int] gcd (immutable): 기약분수로 만들기 위해서 계산한 예비 분모, 분자의 최대 공약수
let gcd: Int = getGCD(dOfReducedFraction, nOfReducedFraction)

// 예비 기약분수의 분자와 분모를 gcd로 나누어 기약분수로 만들어 출력
print("\(nOfReducedFraction/gcd) \(dOfReducedFraction/gcd)")