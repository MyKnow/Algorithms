def solution(s):
    if len(s) == 1:
        return 1

    min_length = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        count = 1

        for i in range(step, len(s), step):
            current = s[i:i+step]
            if current == prev:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = current
                count = 1

        # 마지막 남은 것 처리
        compressed += (str(count) + prev) if count > 1 else prev

        # 최소 길이 갱신
        min_length = min(min_length, len(compressed))

    return min_length
