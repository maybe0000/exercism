def rotate(text, key):
    cipher = ''
    for element in text:
        if element.isalpha():
            if element.isupper():
                cipher += chr(65+(ord(element) - 65 + key)%26)
            else:
                cipher += chr(97+(ord(element) - 97 + key)%26)
        else:
            cipher += element
    return cipher
