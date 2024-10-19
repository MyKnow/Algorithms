# T: Number of Test cases
T = int(input())

for i in range(1, T+1) :
    # A, B : Numbers to be used for Addition
    A, B = map(int, input().split())
    
    print(f"Case #{i}: {A} + {B} = {A+B}")