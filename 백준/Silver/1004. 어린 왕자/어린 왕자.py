testCase = int(input())

def inner (x, y, cx, cy, r):
    distance = (x-cx)**2 + (y-cy)**2
    
    return distance < r**2

for i in range(testCase):
    x1, y1, x2, y2 = map(int, input().split())
    
    numberOfPlanet = int(input())
    
    result = 0
    
    for j in range(numberOfPlanet) :
        cx, cy, r = map(int, input().split())
        
        startPointInTheCircle = inner(x1, y1, cx, cy, r)
        endPointInTheCircle = inner(x2, y2, cx, cy, r)
        
        if (startPointInTheCircle and not(endPointInTheCircle)) :
            result += 1
        elif (not(startPointInTheCircle) and endPointInTheCircle) :
            result += 1
            
    print(result)