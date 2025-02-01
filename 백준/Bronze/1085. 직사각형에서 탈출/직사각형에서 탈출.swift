// [Int] x, y, w, h (immutable)
// x, y: 한수가 위치한 좌표
// w, h: 직사각형 오른쪽 위 꼭짓점의 좌표
// 범위:
// 1 <= x <= w-1 <= 1,000 (자연수)
// 1 <= y <= h-1 <= 1,000 (자연수)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1 2 2").split(separator: " ").map { Int($0) ?? 2}
let x: Int = arrayOfInput[0]
let y: Int = arrayOfInput[1]
let w: Int = arrayOfInput[2]
let h: Int = arrayOfInput[3]

// 한수는 길이가 w, h인 직사각형 내부에만 위치한다.
// 따라서 x-0, y-0, w-x, h-y 중에서 가장 작은 값을 출력하면 된다.
print([x-0, y-0, w-x, h-y].min() ?? "0")