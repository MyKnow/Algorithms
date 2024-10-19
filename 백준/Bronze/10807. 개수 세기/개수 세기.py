# N: Size of Integer Array
N = int(input())

# array: Integer Array
array = list(map(int, input().split()))
    
# v: number for find
v = int(input())

# count: count of found v
count = 0
for i in range(0, N) :
    if array[i] == v :
        count += 1
        
# Another Solution with Array Method
# count = array.count(v)

print(count)
    