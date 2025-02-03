// [Int] N (immutable): 분해합 (범위(자연수): 1 <= N <= 1,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfN (immutable): N의 각 자릿수를 따로 저장한 배열
let arrayOfN: Array<Int> = String(N).compactMap { Int(String($0)) }

// 1. 분해합의 생성자 M은 분해합 N의 길이보다 1 작거나 같다.
// 2. 생성자 M의 범위: (1 <= M <= N)
// 3. 여기서, 단순히 1부터 시작하는 게 아니라, N - (분해합의 자릿수*9)에서 시작하면 의미없는 계산을 생략할 수 있다.
// [Int] start (immutable): 생성자 BruteForce의 최소 범위
let start: Int = [1, N - 9 * arrayOfN.count].max() ?? 1

var isFound = false
for number in start..<N {
    // [Array<Int>] arrayOfM (immutable): number의 각 자릿수를 따로 저장한 배열
    let arrayOfM: Array<Int> = String(number).compactMap { Int(String($0)) }
    
    if (number+arrayOfM.reduce(0, +) == N) {
        print(number)
        isFound = true
        break
    } 
}

if (isFound == false) {
    print(0)
}