// [Array<Int>] numberOfNowPiece (immutable) : 동혁이가 찾은 흰색 체스 기물 개수의 정수 배열 (0 <= Int <= 10, 길이: 6)
let numberOfNowPiece: Array<Int> = (readLine() ?? "0 0 0 0 0 0").split(separator: " ").map {Int($0) ?? 0}

// [Array<Int>] numberOfRequiredPieces (immutable) :
// 체스 기물 중에서
// 킹과 퀸은 1개
// 룩, 비숍, 나이트는 2개
// 폰은 8개
// 이므로, 제약 조건을 설정하는 배열을 생성한다. (길이: 6)
let numberOfRequiredPieces: Array<Int> = [1, 1, 2, 2, 2, 8]

// [Array<Int>] difference (immutable) : 두 배열의 차를 저장하는 배열 (길이: 6)
let difference: Array<Int> = zip(numberOfRequiredPieces, numberOfNowPiece).map { $0 - $1 }

// difference 출력
for number in difference {
    print(number, terminator: " ")
}
