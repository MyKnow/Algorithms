// [Int] N (immutable): 정렬하려는 자연수 (범위(자연수): <= 1,000,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<String>] arrayOfN (immutable): 자연수를 배열로 변환하여 내림차순 정렬함.
let arrayOfN: Array<String> = Array(String(N)).sorted().reversed().map { String($0) }

// 출력 형식에 맞게 변환
print(arrayOfN.joined(separator:""))