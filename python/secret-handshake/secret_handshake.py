actions = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump",
    4: "reverse"
}

def commands(binary_str):
    res = []
    for index, element in enumerate(reversed(binary_str)):
        if element == '1':
            res.append(actions[index])
    if len(res) != 0 and res[-1] == "reverse":
        return list(reversed(res[:-1]))
    return res
