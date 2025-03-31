S = input()

q = int(input())

pSum = dict()
for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)

    if a not in pSum:
        tmpList = list()
        for c in S:
            last = 0 if len(tmpList) == 0 else tmpList[-1]
            if c == a:
                tmpList.append( last + 1 )
            else:
                tmpList.append( last )
        pSum[a] = tmpList

    if l-1 < 0:
        print(pSum[a][r])
    else:
        print(pSum[a][r] - pSum[a][l-1])