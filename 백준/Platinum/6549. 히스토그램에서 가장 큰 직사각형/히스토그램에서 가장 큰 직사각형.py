def solution(hi: list[int]):
    hi.append(0)
    stack = []
    maxArea = 0

    for idx in range(len(hi)):
        currentIdx = idx
        
        while stack and stack[-1][1] >= hi[idx]:
            currentIdx, currentHeight = stack.pop()
            maxArea = max(maxArea, (idx-currentIdx) * currentHeight)
        
        stack.append ( (currentIdx, hi[idx]) )
        
    print(maxArea)
        

while True:
    line = list(map(int, input().split()))

    n = line[0]

    if n == 0:
        break
        
    squares = line[1:]

    solution(squares)