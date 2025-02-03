// [Int] N (immutable): 카드의 개수 (범위: 3 <= N <= 100)
// [int] M (immutable):: 딜러가 외치는 숫자 (범위: 10 <= M <= 300,000)
let arrayOfInput: Array<Int> = (readLine() ?? "3 10").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Array<Int>] arrayOfCards (immutable): 카드들을 저장하는 배열 (길이: N, 범위(자연수): < 100,000)
let arrayOfCards: Array<Int> = (readLine() ?? "1 2").split(separator: " ").compactMap { Int($0) }

// arrayOfCards에 들어있는 카드 중 3개를 골라서 M에 최대한 근접하게 만들고, 그 합을 출력해야 한다.
// 시간 제한이 넉넉하므로, 삼중 중첩 반복문을 만들어서 모든 경우의 수를 계산하여 리스트에 저장하고, M에 근접한 값을 출력한다.

// [Array<Int>] arrayOfSums (mutable):: 카드 3개의 합을 저장하는 배열 (길이: 3)
var arrayOfSums: Array<Int> = [Int]()

for first in arrayOfCards {
    for second in arrayOfCards {
        for third in arrayOfCards {
            // 동일한 카드가 아닌 경우에만 배열에 더한다.
            if (first != second && second != third && first != third) {
                arrayOfSums.append(first+second+third)
            }
        }
    }
}

// [Int] index (mutable): 현재 리스트의 인덱스
var index: Int = 0

// 합계 리스트를 내림차순 정렬하고, M보다 작거나 같은 수를 찾을 때까지 index를 더한다.
let sortedArray: Array<Int> = arrayOfSums.sorted(by: { $0 > $1} )
while(sortedArray[index] > M) {
    index+=1
}
    
    
// 해당 index-1에 있는 요소를 출력한다.
print(sortedArray[index])