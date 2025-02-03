// [Int] a1, a0 (immutable): 함수 f(n)을 나타내는 정수 (범위(정수): 0 ≤ |a_i| ≤ 100)
let arrayOfInput: Array<Int> = (readLine() ?? "0 0").split(separator: " ").compactMap { Int($0) }
let (a1, a0): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Int] c (immutable): 양의 정수 (범위(정수): 1 ≤ c ≤ 100)
let c: Int = Int(readLine() ?? "1") ?? 1

// [Int] n0: 양의 정수 (범위(정수): 1 ≤ n0 ≤ 100)
let n0: Int = Int(readLine() ?? "1") ?? 1

// f(n) = a1*n + a0
// f(n) <= c * g(n) (모든 n은 n0 이상)
// 위 두 조건을 만족할 경우 1, 아니면 0을 출력하면 된다.
// 이 때, a0이 음의 정수일 때 예외가 생길 수 있다.
// 따라서, a1이 c보다 작거나 같아야 한다는 예외 조건을 추가해야 한다.

// [Int] fn (immutable): fn 함수값
let fn: Int = a1 * n0 + a0

if (fn <= c * n0 && a1 <= c) {
    print(1)
}
else {
    print(0)
}