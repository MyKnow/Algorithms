from sys import stdin, stdout

readline = stdin.readline

def getNumber(ch):
    return ord(ch)-ord("A")+1

def getString(lst):
    tmp = ""
    for l in lst:
        tmp += chr(l+ord("A")-1)
    return tmp

def getPrimaryNumberList(n):
    result = [1]

    if n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                result.append(i)
    return result
    
plainText = readline().rstrip()
cipherText = readline().rstrip()

result = []
for p, c in zip(plainText, cipherText):
    dif = getNumber(c) - getNumber(p)
    result.append(dif if dif > 0 else getNumber(c)+26-getNumber(p))

length = len(plainText)
for l in getPrimaryNumberList(length):
    setOfCut = set()

    for i in range(0, length-l+1, l):
        cut = result[i:i+l]
        setOfCut.add(getString(cut))

    if len(setOfCut) == 1:
        print(setOfCut.pop())
        break