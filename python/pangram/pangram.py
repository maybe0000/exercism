def is_pangram(sentence):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cleaned_sentence = ''.join([char for char in sentence if char.isalpha()])
    #return alphabet == ''.join(sorted(set(''.join(cleaned_sentence.split(' ')).upper())))
    return alphabet == ''.join(sorted(set(cleaned_sentence.upper())))