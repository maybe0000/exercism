def flatten(iterable):
    flattened_arr = []
    for el in iterable:
        if isinstance(el, list):
            flattened_arr.extend(flatten(el))
        elif el is None:
            continue
        else:
            flattened_arr.append(el)
    return flattened_arr