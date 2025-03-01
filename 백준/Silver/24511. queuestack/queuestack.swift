// [Int] N (immutable): 자료구조의 개수 (범위(자연수): 1 ≤ N ≤ 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<String>] A (immutable): 각 자리의 자료구조의 형태를 나타내는 수열 (0: 큐, 1: 스택, 길이: N)
let A: [String] = (readLine() ?? "0").split(separator: " ").compactMap { String($0) }

// [Array<String>] B (immutable): 각 자리의 자료구조의 초기값 (길이: N, 범위(자연수): 1 ≤ B_i ≤ 1,000,000,000)
let B: [String] = (readLine() ?? "0").split(separator: " ").compactMap { String($0) }

// [Int] M (immutable): 삽입할 수열의 길이 (범위(자연수): 1 ≤ M ≤ 100,000)
let M: Int = Int(readLine() ?? "1") ?? 1

// [Array<String>] C (immutable): queuestack에 삽입할 원소를 담은 길이 M의 수열 (길이: M, 범위(자연수): 1 ≤ C_i ≤ 1,000,000,000)
let C: [String] = (readLine() ?? "0").split(separator: " ").compactMap { String($0) }

// [Array<String>] bWithoutStack (mutable): Stack 부분이 제외된 수열 B를 나타내는 배열
var bWithoutStack: [String] = [String]()

for index in 0..<A.count {
    if (A[index] == "0") {
        bWithoutStack.append(B[index])
    }
}

// 두 배열을 합친 다음, 길이 M만큼 출력한다.
print((bWithoutStack.reversed() + C)[0..<M].joined(separator: " "))