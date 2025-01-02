// N: Int (immutable) - 세준이가 시험을 본 과목의 개수 (1 <= N <= 1000)
let N = Int(readLine() ?? "1") ?? 1

// scoreArr: Array<Double> (immutable) - 세준이의 시험 점수들 (길이: N, 0 < score <= 100)
let scoreArr = (readLine() ?? "").split(separator: " ").compactMap { Double($0) }

// M: Double (immutable) - 세준이의 시험 점수 중 최고점 (0 < M <= 100)
let M = scoreArr.max() ?? 1.0

// 변환 점수를 바로 합산하여 평균을 계산
let sumOfReplacedScores = scoreArr.reduce(0.0) { $0 + ($1 / M * 100) }
let average = sumOfReplacedScores / Double(N)

// 평균 출력 (소수점 이하 출력)
print(average)