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
            
            # 최소성 검증
            if any(set(c).issubset(set(comb)) for c in candidates):
                continue
            
            # 유일성 검증
            row_set = set(tuple(row[i] for i in comb) for row in relation)
            if len(row_set) == row_count:
                candidates.append(set(comb))
                
    return len(candidates)