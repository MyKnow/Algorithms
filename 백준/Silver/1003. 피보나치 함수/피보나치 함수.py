arr = [[-1 for i in range(40)] for _ in range(3)]

countOfZero = 0
countOfOne = 0

def fibonacci(n):
    global countOfZero, countOfOne
    
    if (n==0):
        countOfZero+=1
        return 0
    elif (n==1):
        countOfOne+=1
        return 1
    else :
        if (arr[2][n] != -1) :
            countOfZero+=arr[0][n]
            countOfOne+=arr[1][n]
            return arr[2][n]
        else :
            arr[2][n] = fibonacci(n-1) + fibonacci(n-2)
            arr[0][n] = countOfZero
            arr[1][n] = countOfOne
            return arr[2][n]
    
testCase = int(input())

for i in range(testCase):
    countOfZero = 0
    countOfOne = 0
    arr = [[-1 for i in range(41)] for _ in range(3)]
    
    n = int(input())
    
    fibonacci(n)
    
    print(str(countOfZero) + " " + str(countOfOne))
        

