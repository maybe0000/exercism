def find_anagrams(word, candidates):
    anagrams = []
    for w in candidates:
        if w.lower() == word.lower():
            continue
        elif ''.join(sorted(list(word.lower()))) == ''.join(sorted(list(w.lower()))):
            anagrams.append(w)
    return anagrams 
