def decode(string):
    # 1. If current character is digit, find j, the last index of successive digits
    #   2. Turn that sequence of digits into int
    #   3. Store character after last digit into variable c
    #   4. Append into result character multiplied by int from 2.
    #   5. Transition to position j+2
    # 2. If current character is not digit, add to result
    if string == "":
        return ""
    res = ""
    multiply = ""
    for i in range(len(string)):
        if string[i].isdigit():
            multiply += string[i]
        else:
            res += string[i] * (int(multiply) if multiply != "" else 1)
            multiply = ""
    return res


def encode(string):
    # 1. Counting number of occurences of first character
    #   i. Set count to 1
    #   ii. As long as next character is equal, increase counter
    #   iii. If not equal, add character and count to result
    # 2. Count number of occurences of next character
    #   i. - iii. same as 1.
    if string == "":
        return ""
    res = ""
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            res += (str(count) if count > 1 else "") + string[i - 1]
            count = 1
    res += (str(count) if count > 1 else "") + string[i]
    return res
