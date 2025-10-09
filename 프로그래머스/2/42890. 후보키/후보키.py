from itertools import combinations

def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])
    candidates = []
    
    # 조합은 1개부터 col개까지 존재
    for i in range(1, col_count+1):
        # 중복없는 조합 생성
        for comb in combinations(range(col_count), i):
            seen = set()
            
            for row in relation:
                value = tuple(row[i] for i in comb)
                seen.add(value)
                
            # 유일성 검증
            if len(seen) < row_count:
                continue
                
            # 최소성 검증
            flag = True
            for c in candidates:
                if set(c).issubset(set(comb)):
                    flag = False
                    break
            
            if flag:
                candidates.append(set(comb))
                
    return len(candidates)