def is_valid(isbn):
    isbn_wo_dashes = isbn.replace('-','')
    if len(isbn_wo_dashes) != 10:
        return False
    # if ''.join([digit for digit in isbn_wo_dashes[:-1] if not digit.isdigit()]):
    #     return False
    if any(not c.isdigit() for c in isbn_wo_dashes[:-1]):
        return False
    if isbn_wo_dashes[-1] == 'X':
        d10 = 10
    elif isbn_wo_dashes[-1].isdigit():
        d10 = int(isbn_wo_dashes[-1])
    else:
        return False
    #return (int(isbn_wo_dashes[0]) * 10 + int(isbn_wo_dashes[1]) * 9 + int(isbn_wo_dashes[2]) * 8 + int(isbn_wo_dashes[3]) * 7 + int(isbn_wo_dashes[4]) * 6 + int(isbn_wo_dashes[5]) * 5 + int(isbn_wo_dashes[6]) * 4 + int(isbn_wo_dashes[7]) * 3 + int(isbn_wo_dashes[8]) * 2 + d10 * 1) % 11 == 0
    return (sum(int(isbn_wo_dashes[i]) * (10 - i) for i in range(9)) + d10 * 1) % 11 == 0
