/// [func] getResultWithoutMethod
/// 
/// # Notes
/// - min, max 함수 없이 최소값, 최대값을 산출해내는 함수
/// 
/// # Parameters
/// - Array<Int> targetArray : 값을 산출하고자 하는 정수 배열
/// 
/// # Returns
/// - Array<Int> result : [minOfArray, maxOfArray]
/// 
func getResultWithoutMethod(targetArray: Array<Int>) -> Array<Int> {
    // [Int] minOfArray : 배열의 최소값을 저장하는 변수 (입력의 상한선으로 초기화)
    var minOfArray: Int = 1000000
    // [Int] maxOfArray : 배열의 최대값을 저장하는 변수 (입력의 하한선으로 초기화)
    var maxOfArray: Int = -1000000
    
    for i in 0..<targetArray.count {
        if (targetArray[i] < minOfArray) {
            minOfArray = targetArray[i]
        }
        if (targetArray[i] > maxOfArray) {
            maxOfArray = targetArray[i]
        }
    }
  
    return [minOfArray, maxOfArray]
}

/// [func] getResultWithMethod
/// 
/// # Notes
/// - min, max 함수를 사용하여 최소값, 최대값을 산출해내는 함수
/// 
/// # Parameters
/// - Array<Int> targetArray : 값을 산출하고자 하는 정수 배열
/// 
/// # Returns
/// - Array<Int> result : [minOfArray, maxOfArray]
/// 
func getResultWithMethod(targetArray: Array<Int>) -> Array<Int> {
    // [Int] minOfArray : 배열의 최소값을 저장하는 변수
    var minOfArray: Int = (targetArray.min() ?? 0)
    // [Int] maxOfArray : 배열의 최대값을 저장하는 변수
    var maxOfArray: Int = (targetArray.max() ?? 0)
  
    return [minOfArray, maxOfArray]
}


// [Int] N : 정수의 개수 (1 <= N <= 1,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arr : Int를 저장하는 배열 (-1,000,000 <= int <= 1,000,000)
let arr: Array<Int> = (readLine() ?? "0").split(separator: " ").map{Int($0) ?? 0}

let resultArr = getResultWithMethod(targetArray: arr)

print(resultArr[0], resultArr[1])