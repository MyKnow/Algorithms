// [Int] N (immutable): 주어진 수의 개수 (범위: <= N)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Int] countOfPrime (mutable): 소수의 개수를 세는 변수
var countOfPrime: Int = 0

// [Array<Int>] numberList (mutable): 검사할 숫자들을 담는 리스트 (범위: <= 1,000, 길이: N)
var numberList: Array<Int> = (readLine() ?? "1").split(separator: " ").map { Int($0) ?? 1}

// [func(Int)->Bool] isPrime: 소수인지 판별하는 함수
func isPrime(_ num: Int) -> Bool {
    // 1 이하는 소수가 아님
    if (num < 2) { return false }
    
    // 2부터 num-1까지 수 중에서 나누어 떨어지는 수가 있으면 소수가 아님.
    for i in 2..<num {
        if num % i == 0 {
            return false
        }
    }
    return true
}

for number in numberList {
    if (isPrime(number)) {
        countOfPrime+=1
    }
}
            
// 소수의 개수를 출력한다.
print(countOfPrime)