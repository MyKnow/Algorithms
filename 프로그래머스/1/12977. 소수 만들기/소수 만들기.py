from math import ceil

def solution(nums):
    answer = 0
    
    length = len(nums)
    
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if isPrimeNumber(nums[i] + nums[j] + nums[k]):
                    answer += 1

    return answer

def isPrimeNumber(n):
    rootN = ceil(n ** 0.5)
    
    for i in range(2, rootN+1):
        if n % i == 0:
            return False
    
    return True