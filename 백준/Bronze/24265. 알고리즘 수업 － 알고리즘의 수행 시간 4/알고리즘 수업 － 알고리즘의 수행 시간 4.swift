// 시간복잡도는 O(n^2)이므로 최고차항의 차수는 2이다.
// 수행 횟수는 (n-1)! 이다.

// [Int] n (immutable): 입력의 크기 (범위: 1 ≤ n ≤ 500,000)
let n: Int = Int(readLine() ?? "1") ?? 1

// [Int] exeCount (mutable): 수행 횟수를 저장하는 변수
var exeCount: Int = 0

for i in 1..<n {
    exeCount += i
}

print("\(exeCount)\n2")