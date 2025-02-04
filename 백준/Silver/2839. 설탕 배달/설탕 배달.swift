// [Int] N (immutable): 배달해야 하는 설탕의 무게 (범위(자연수): 3 <= N <= 5,000)
let N: Int = Int(readLine() ?? "3") ?? 3

// [Int] count (mutable): 봉지의 수
var count: Int = 0

// [Int] remainingWeight (mutable): 남은 설탕의 무게
var remainingWeight: Int = N

// 남은 설탕이 없어질 때까지 반복
while (remainingWeight >= 0) {
    // 현재 5kg 봉지로 모두 담을 수 있다면 바로 종료
    if (remainingWeight % 5 == 0)  {
        // 현재 봉지 수에 5kg 봉지를 모두 더한다.
        count += remainingWeight / 5
        print(count)
        break
    }
    // 5kg 봉지로 다 담을 수 없다면, 3kg 봉지로 담는다.
    count += 1
    remainingWeight -= 3
}

// 만약 남은 설탕이 음수라면, 정확하게 만들 수 없는 것이므로 -1 출력
if (remainingWeight < 0) {
    print(-1)
}