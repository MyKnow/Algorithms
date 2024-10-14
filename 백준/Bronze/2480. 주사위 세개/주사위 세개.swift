let inputArray: [Int] = (readLine() ?? "1 1 1").split(separator: " ").map{ Int($0) ?? 1 }

// 주사위 눈 : 1 <= diceN <= 6
let dice1: Int = inputArray[0]
let dice2: Int = inputArray[1]
let dice3: Int = inputArray[2]

// 주사위 눈 3개가 똑같은 경우
if (dice1 == dice2 && dice2 == dice3) {
    print(10000+dice1*1000)
} 
// 주사위 모두 다른 눈이 나오는 경우
else if (dice1 != dice2 && dice2 != dice3 && dice1 != dice3) {
    let maxNumber: Int = inputArray.max() ?? 1
    print(maxNumber*100)
}
// 주사위 눈 2개만 똑같은 경우
else {
    let pairDiceNumber: Int = (dice1 == dice2 || dice1 == dice3) ? dice1 : dice2
    
    print(1000+pairDiceNumber*100)
}
