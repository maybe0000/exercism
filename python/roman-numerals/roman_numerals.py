numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
names = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def roman(number: int) -> str:
    res = []

    for i, val in enumerate(numbers):
        while number >= val:
            res.append(names[i])
            number = number - val

    return "".join(res)
