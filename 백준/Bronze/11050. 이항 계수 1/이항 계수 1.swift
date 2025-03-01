// [func<Int> -> Int] factorial: 주어진 정수의 팩토리얼을 계산하여 반환하는 함수
func factorial(_ target: Int) -> Int {
    var temp: Int = 1
    
    for n in 1...max(target, 1) {
        temp *= n
    }
    
    return temp
}
        
// [Int] N, K: 이항 계수를 구하기 위한 자연수와 정수 
// K 범위: 0 <= K <= N
// N 범위: 1 <= N <= 10
let arrayOfInput: [Int] = (readLine() ?? "1 0").split(separator: " ").compactMap { Int($0) }
let (N, K): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// 이항계수 == nCk
// 즉, n개에서 k를 뽑는 조합의 개수를 의미한다.
// 공식에 따라서 n-k!를 구하고 k!와 곱한 다음, 이를 n!과 나눈 결과를 반환하면 된다.
print(factorial(N) / (factorial(N-K) * factorial(K)))