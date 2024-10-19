# T : Number of test cases
T = int(input())

for i in range(1, T+1):
    # A, B : Integers to be used in addition
    A, B = map(int, input().split())
    
    print(f"Case #{i}: {A+B}")