def is_isogram(string):
    clean_string = ''.join([char for char in string if char.isalpha()]).upper()
    return len(clean_string) == len(set(clean_string))