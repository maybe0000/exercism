def is_paired(input_string):
    cleaned_str = ''.join(c if c in ('(',')','[',']','{','}') else '' for c in input_string)
    if cleaned_str == '':
        return True
    closed_to_open = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open_brackets = []
    for c in input_string:
        if c in ('(', '[', '{'):
            open_brackets.append(c)
        if c in closed_to_open:
            if not open_brackets or open_brackets[-1] != closed_to_open[c]:
                return False
            else:
                open_brackets.pop()
    return not bool(open_brackets)