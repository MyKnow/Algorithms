// [Int] lenOfDivisor (immutable): 약수의 개수 (범위(자연수): 1 <= N <= 50)
if let N: Int = Int(readLine() ?? "1") {
    // [Array<Int>] arrayOfDivisor (immutable): 1과 N을 제외한 N의 약수를 오름차순 정렬한 배열
    // 범위(자연수): 2 <= divisor <= 1,000,000, 중복없음.
    let arrayOfDivisor: [Int] = (readLine() ?? "2")
            .split(separator: " ")
            .compactMap { Int($0) }
            .sorted()

    // 첫번째와 마지막 요소를 서로 곱하면 원래 수가 나온다.
    if let first = arrayOfDivisor.first, let last = arrayOfDivisor.last {
        print(first * last)
    }
}
