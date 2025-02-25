def is_paired(input_string):
    cleaned_str = ''.join(c if c in ('(',')','[',']','{','}') else '' for c in input_string)
    if cleaned_str == '':
        return True
    count_open = {
        c: 0 for c in ('(','{','[')
    }
    closed_to_open = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open_brackets = []
    for c in input_string:
        if c in count_open:
            open_brackets.append(c)
            count_open[c] += 1
        if c in closed_to_open:
            if not open_brackets or open_brackets[-1] != closed_to_open[c]:
                return False
            else:
                open_brackets.pop()
            count_open[closed_to_open[c]] -= 1
        if (c in count_open and count_open[c] < 0) or (c in closed_to_open and count_open[closed_to_open[c]] < 0):
                return False
    return all(value == 0 for value in count_open.values())