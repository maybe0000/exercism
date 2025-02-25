def translate(text: str):
    def translate_one_word(word: str):
        if word.startswith(('a','e','i','o','u','xr','yt')):            
            return word+'ay'
        qu = word.find('qu')
        if qu >= 0 and all(vowel not in word[:qu] for vowel in 'aeiou'):
            return word[qu+2:]+word[:qu+2]+'ay'
        y = word.find('y')
        if y >= 0 and all(vowel not in word[:y] for vowel in 'aeiou') and not word.startswith('y'):
            return word[y:]+word[:y]+'ay'
        def first_vowel(word):
            for i, c in enumerate(word):
                if c in 'aeiou':
                    return i
            return -1
        fw = first_vowel(word)
        if fw >= 0:
            return word[fw:]+word[:fw]+'ay'
        return word
    
    sentence_arr = []
    
    for word in text.split(' '):
        sentence_arr.append(translate_one_word(word))
        
    return ' '.join(sentence_arr)
    