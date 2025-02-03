// [Array<Int>] arrayOfSticks (immutable): 삼각형을 만들기 위한 세 막대 배열 (범위(정수): 1 <= a, b, c <= 100)
let arrayOfSticks: Array<Int> = (readLine() ?? "1 1 1").split(separator: " ").compactMap { Int($0) }

// [Set(int)] setOfSticks (mutable): 막대들을 저장하는 Set
var setOfSticks: Set<Int> = Set<Int>(arrayOfSticks)

// [Int] maxOfSticks (immutable): 가장 긴 막대의 길이
let maxOfSticks: Int = arrayOfSticks.max() ?? 0

// [Int] minOfSticks (immutable): 가장 짧은 막대의 길이
let minOfSticks = arrayOfSticks.min() ?? 0

// 1. a, b, c가 모두 동일하다면 정삼각형을 만들 수 있다.
if (setOfSticks.count == 1) {
    print(minOfSticks * 3)
}

// 2. 세 막대 중 같은 길이가 2개 있을 때
else if (setOfSticks.count == 2) {
    // 2-1. 같은 길이의 막대가 나머지 막대보다 짧다면 긴 막대의 길이를 줄인다.
    if (arrayOfSticks.filter { $0 == minOfSticks }.count == 2) {
        print(minOfSticks * 2 + (minOfSticks * 2 - 1))
    }
    // 2-2. 같은 길이의 막대가 나머지 막대보다 길다면 그대로 출력
    else {
        print(maxOfSticks * 2 + minOfSticks)
    }
}

// 3. 세 막대 모두 길이가 다를 경우
else {
    // [Int] midOfSticks (immutable): 중간 길이의 막대 (리스트에서 정렬하여 구하기)
    let midOfSticks: Int = arrayOfSticks.sorted()[1]

    // 3-1. 삼각형이 가능한 경우 그냥 출력
    if (minOfSticks + midOfSticks > maxOfSticks) {
        print(arrayOfSticks.reduce(0, +))
    }
    // 3-2. 삼각형을 못 그릴 경우 긴 막대를 줄여서 출력
    else {
        print((minOfSticks + midOfSticks) * 2 - 1)
    }
}