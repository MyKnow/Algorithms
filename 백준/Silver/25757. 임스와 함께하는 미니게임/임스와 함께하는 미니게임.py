# N, G
# N: 임스와 같이 플레이하기를 신청한 횟수(1 <= N <= 100_000)
# G: Y, F, O (2, 3, 4명 동시 게임)
N, G = input().split()
N = int(N)

game = {"Y": 1, "F": 2, "O": 3}

names = dict()
for _ in range(N):
    name = input()

    if name in names:
        names[name] += 1
    else:
        names[name] = 1

print(len(names) // game[G])