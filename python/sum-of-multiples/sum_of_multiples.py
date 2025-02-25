def sum_of_multiples(limit: int, multiples: list):
    def multiples_of_smaller_than(multiple: int, limit: int):
        cur = multiple
        list_of_multiples = []
        if cur == 0:
            return list_of_multiples
        while cur < limit:
            list_of_multiples.append(cur)
            cur += multiple
        return list_of_multiples
    
    full_list = []

    for m in multiples:
        full_list += multiples_of_smaller_than(m, limit)
    
    return sum(set(full_list))