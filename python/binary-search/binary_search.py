def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
    left, right = 0, len(search_list) - 1
    while left <= right:
        middle_index = (left + right) // 2
        mid = search_list[middle_index]
        print(f'left: {left}, middle: {middle_index}, right: {right}')
        if value > mid:
            left = middle_index + 1
        elif value < mid:
            right = middle_index - 1
        elif value == mid:
            return middle_index
    raise ValueError("value not in array")