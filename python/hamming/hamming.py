def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    diff_cnt = 0
    for index, char in enumerate(strand_a):
        if strand_a[index] != strand_b[index]:
            diff_cnt += 1
    return diff_cnt
#     return sum(a != b for a, b in zip(strand_a, strand_b))
