def proverb(*inputList, qualifier=None):
    res = []
    if len(inputList) == 0:
        return []
    inputList = list(inputList)
    if len(inputList) >= 2:
        for i in range(len(inputList) - 1):
            res.append(
                f"For want of a {inputList[i]}" + f" the {inputList[i + 1]} was lost."
            )
    res.append(
        f"And all for the want of a {qualifier + ' ' + inputList[0] if qualifier else inputList[0]}."
    )
    return res
