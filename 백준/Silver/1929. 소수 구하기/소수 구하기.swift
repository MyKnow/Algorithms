import Foundation

// [func(Int)->Array<Int>] getPrimeNumberArray: 1,000,000 이하의 소수로 구성된 배열
func getPrimeNumberArray(_ integer: Int) -> Array<Int> {
    // [Array<Bool>] boolArray (mutable): 0부터 1,000,000까지의 index를 가지는 배열 (길이: 1,000,001)
    var boolArray: Array<Bool> = [Bool](repeating: true, count: integer+1)
    
    // [Int] sqrtInt (immutable): 제곱근이 취해진 integer
    let sqrtInt: Int = Int(Double(integer+1).squareRoot())
    
    // 2부터 자기자신까지 소수가 존재하는 지 검사
    for n in 2...sqrtInt+1 {
        // boolArray의 n번째 요소가 소수라면, n의 배수들은 소수가 아니다.
        if (boolArray[n]) {
            var i: Int = 2
            
            while (n * i <= integer) {
                boolArray[n*i] = false
                i+=1
            }
        }
    }
    
    // offset이 2 이상이고, element가 true인 offset를 정수 배열로 묶어서 반환
    return boolArray.enumerated().filter { $0.offset >= 2 && $0.element }.map { $0.offset }
}

// [Int] M, N (immutable): 소수를 찾을 정수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 1,000,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (M, N): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// getPrimeNumberArray에서 얻은 배열에서 M과 N 사이의 값만 출력
print(getPrimeNumberArray(N).filter { (M...N).contains($0) }.map { String($0) }.joined(separator: "\n"))