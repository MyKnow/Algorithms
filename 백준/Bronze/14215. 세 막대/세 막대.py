# [list(int)] listOfSticks: 삼각형을 만들기 위한 세 막대 리스트 (범위(정수): 1 <= a, b, c <= 100)
listOfSticks = list(map(int, input().split()))

# [set(int)] setOfSticks: 막대들을 저장하는 Set
setOfSticks = set(listOfSticks)

# [int] maxOfSticks: 가장 긴 막대의 길이
maxOfSticks = max(listOfSticks)

# [int] minOfSticks: 가장 짧은 막대의 길이
minOfSticks = min(listOfSticks)

# 1. a, b, c가 모두 동일하다면 정삼각형을 만들 수 있다.
if len(setOfSticks) == 1:
    print(minOfSticks * 3)

# 2. 세 막대 중 같은 길이가 2개 있을 때
elif len(setOfSticks) == 2:
    # 2-1. 같은 길이의 막대가 나머지 막대보다 짧다면 긴 막대의 길이를 줄인다.
    if listOfSticks.count(minOfSticks) == 2:
        maxOfSticks = minOfSticks * 2 - 1
        print(minOfSticks * 2 + maxOfSticks)
    # 2-2. 같은 길이의 막대가 나머지 막대보다 길다면 그대로 출력
    else:
        print(maxOfSticks * 2 + minOfSticks)

# 3. 세 막대 모두 길이가 다를 경우
else:
    # 중간 길이의 막대 찾기 (리스트에서 정렬하여 구하기)
    sortedSticks = sorted(listOfSticks)
    midOfSticks = sortedSticks[1]  # 중간 값

    # 3-1. 삼각형이 가능한 경우 그냥 출력
    if minOfSticks + midOfSticks > maxOfSticks:
        print(sum(listOfSticks))
    # 3-2. 삼각형을 못 그릴 경우 긴 막대를 줄여서 출력
    else:
        print((minOfSticks + midOfSticks) * 2 - 1)