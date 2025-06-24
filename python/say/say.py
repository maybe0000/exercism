digit_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
}

reversed_dict = dict(reversed(digit_dict.items()))

tens = {i * 10 for i in range(1, 10)}


def say(number):
    if number < 0 or number > 999999999999 or type(number) is not int:
        raise ValueError("input out of range")
    if number < 100 and number in reversed_dict:
        # print(number)
        return reversed_dict[number]
    for div_by, word in reversed_dict.items():
        r, m = divmod(number, div_by)
        if r == 0:
            continue
        # prefix + " " + "million" + " " + suffix
        # 131 million 190
        # one hundred thirty-one million one hundred ninety
        is_ten = r * div_by in tens
        prefix = "" if r == 1 and is_ten else say(r)
        suffix = "" if m == 0 else say(m)
        # 31
        # r = 1, m = 1
        # is_ten = true
        # prefix = ""
        # suffix = "one"
        # word = "thirty"
        res = (
            word + "-" + suffix
            if is_ten
            else " ".join(filter(bool, [prefix, word, suffix]))
        )
        # print(number, res)
        return res
