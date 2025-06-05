from sys import stdin

readline = stdin.readline

def getNumber(ch):
    return ord(ch) - ord("A") + 1

def getString(lst):
    return "".join(chr(x + ord("A") - 1) for x in lst)

def getPrimaryNumberList(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)

plain = readline().rstrip()
cipher = readline().rstrip()
length = len(plain)

diffs = [
    (getNumber(c) - getNumber(p)) % 26 or 26
    for p, c in zip(plain, cipher)
]

for l in getPrimaryNumberList(length):
    segment = getString(diffs[:l])
    valid = True
    for i in range(0, length, l):
        if getString(diffs[i:i+l]) != segment:
            valid = False
            break
    if valid:
        print(segment)
        break