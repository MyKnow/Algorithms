import Foundation

// [Int] N (immutable): 녹색거탑의 높이를 나타내는 정수 N (범위(자연수): 1 <= N <= 5)
if let N: Int = Int(readLine() ?? "1") {
    // 한 번 내려갈 때마다 경우의 수가 2개씩 생기므로, 단순히 제곱을 취해주면 된다.
    print(pow(2, N))
}
