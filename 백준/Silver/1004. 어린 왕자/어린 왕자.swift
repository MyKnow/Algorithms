let testCase: Int = Int(readLine() ?? "0") ?? 0

func innerCheckFunction(_ x: Int, _ y: Int, _ cx: Int, _ cy: Int, _ r: Int) -> Bool {
    let distance: Int = ((x-cx)*(x-cx))+((y-cy)*(y-cy))
    
    return distance < (r*r)
}

for _ in 0..<testCase {
    let pointArray: [Int] = (readLine() ?? "0 0 0 0").split(separator: " ").map{Int($0) ?? 0}
    
    let x1 = pointArray[0]
    let y1 = pointArray[1]
    let x2 = pointArray[2]
    let y2 = pointArray[3]
    
    let numberOfPlanet: Int = Int(readLine() ?? "1") ?? 1
    
    var result: Int = 0
  
    for _ in 0..<numberOfPlanet {
        let circleArray: [Int] = (readLine() ?? "1 1 1").split(separator: " ").map{Int($0) ?? 1}
        
        let cx: Int = circleArray[0]
        let cy: Int = circleArray[1]
        let r: Int = circleArray[2]
        
        let startPointInTheCircle: Bool = innerCheckFunction(x1, y1, cx, cy, r)
        let endPointInTheCircle: Bool = innerCheckFunction(x2, y2, cx, cy, r)
        
        if (startPointInTheCircle && !endPointInTheCircle) {
            result += 1
        } else if (!startPointInTheCircle && endPointInTheCircle) {
            result += 1
        }
    }
    
    print(result)
}