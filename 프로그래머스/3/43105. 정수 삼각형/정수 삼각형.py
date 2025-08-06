# 삼각형 좌측 하단 -> x: +0, y: +1
# 삼각형 우측 하단 -> x: +1, y: +1
directions = [
    (0, 1), (1, 1)
]

def solution(triangle):
    maxLen = len(triangle)
    
    # dp[y][x]: 해당 (x, y) 좌표에서 가장 높은 조합을 저장
    dp = [[0 for _ in range(maxLen+1)] for _ in range(maxLen+1)]
    dp[0][0] = triangle[0][0]
    
    for y in range(maxLen-1):
        for x in range(len(triangle[y])):
            triangle[y][x]
            for dx, dy in directions:  
                dp[y+dy][x+dx] = max(dp[y][x] + triangle[y+dy][x+dx], dp[y+dy][x+dx])

    return max(dp[maxLen-1])