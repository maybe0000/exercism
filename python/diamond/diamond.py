def rows(letter):
    if not 65 <= ord(letter) <= 90:
        raise ValueError("Enter a valid uppercase letter.")
    diamond = []
    letter_number = ord(letter) - 65 + 1
    # length_of_diamond = letter_number * 2 - 1
    for index, char in enumerate(range(65, ord(letter) + 1)):
        # print(index, char)
        left_dot_count = letter_number - index - 1
        left_part = " " * left_dot_count + chr(char) + " " * (index - 1)
        diamond.append(
            left_part + (" " if index else "") + left_part[::-1][(0 if index else 1) :]
        )
    diamond += reversed(diamond[:-1])
    # print("\n".join(diamond))
    return diamond
