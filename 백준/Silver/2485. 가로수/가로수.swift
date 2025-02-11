// [func(Int, Int) -> Int] getGCD: 최대 공약수를 반환하는 함수
func getGCD(_ a: Int, _ b: Int) -> Int{
    if (b==0) {
        return a
    }
    else {
        return getGCD(b, a%b)
    }
}

// [Int] N (immutable): 이미 심어져 있는 가로수의 수 (범위(자연수): 3 ≤ N ≤ 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Int] minOfDiff (mutable): 각 가로수 간의 거리 중에서 가장 짧은 간격을 저장하는 변수 (초기값: 1,000,000,000)
var minOfDiff: Int = 1000000000

// [Array<Int>] arrayOfTrees (mutable): 각 가로수의 위치를 저장하는 배열(길이: N)
var arrayOfTrees: Array<Int> = [Int]()

// [Array<Int>] arrayOfDiff (mutable): 각 가로수 간의 거리 차이를 저장하는 배열 (길이: N-1)
var arrayOfDiff: Array<Int> = [Int]()

for index in 0..<N {
    // [Int] nowTree (immutable): 현재 가로수의 위치를 저장하는 변수(범위(자연수): <= 1,000,000,000)
    let nowTree: Int = Int(readLine() ?? "1") ?? 1
    
    // index가 0일 땐 arrayOfTrees에 현재 가로수 위치를 추가만 한다.
    if let lastTree = arrayOfTrees.last {
        // [Int] nowDiff (immutable): 이전 가로수와 현재 가로수 간의 거리 차이
        let nowDiff: Int = nowTree - lastTree
        
        // index가 1일때(2번째 반복 때) nowTree와 첫번째 가로수의 거리 차이를 minOfDiff에 바로 갱신한다.
        // index가 2 이상일 때, 최대 공약수를 통해서 minOfDiff를 갱신한다.
        minOfDiff = (index == 1) ? nowDiff : getGCD(minOfDiff, nowDiff)
        
        // 현재 거리 차이를 arrayOfDiff에 추가한다.
        arrayOfDiff.append(nowDiff)
    }
            
    // arrayOfTrees에 가로수의 위치를 저장한다.
    arrayOfTrees.append(nowTree)
}

// [Int] count (mutable): 새로 심어야 하는 가로수를 저장하는 변수 (초기값: 0)
var count: Int = 0

// arrayOfDiff를 순회하며, count를 증가시킨다.
for diff in arrayOfDiff {
    // diff를 minOfDiff로 나눈 몫에 1을 빼서 count에 더한다.
    // 나머지가 존재하지 않는다고 가정한다.
    count += diff/minOfDiff - 1
}

// count를 출력한다.
print(count)