# [list(int)] numberOfNowPiece : 동혁이가 찾은 흰색 체스 기물 개수 리스트 (0 <= int <= 10)
numberOfNowPiece = list(map(int, input().split()))

# [list(int)] numberOfRequiredPieces :
# 체스 기물 중에서
# 킹과 퀸은 1개
# 룩, 비숍, 나이트는 2개
# 폰은 8개
# 이므로, 제약 조건을 설정하는 리스트를 생성한다.
numberOfRequiredPieces = [1, 1, 2, 2, 2, 8]

# 필요한 수에서 현재 수를 뺀 값을 출력
print(" ".join(str(r-n) for r, n in zip(numberOfRequiredPieces, numberOfNowPiece)))