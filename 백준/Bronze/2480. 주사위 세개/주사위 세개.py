# 각 diceN : 1 <= diceN <= 6
dice1, dice2, dice3 = map(int, input().split())

# 같은 눈이 3개 나오는 경우
if dice1 == dice2 == dice3:
    print(10000 + dice1 * 1000)
# 모두 다른 눈이 나오는 경우
elif dice1 != dice2 != dice3 != dice1:
    print(max(dice1, dice2, dice3) * 100)
# 같은 눈이 2개만 나오는 경우
else:
    pairDiceNumber = dice1 if dice1 == dice2 or dice1 == dice3 else dice2
    print(1000 + pairDiceNumber * 100)