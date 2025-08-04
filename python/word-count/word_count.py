import re


def count_words(sentence):
    import re


def count_words(sentence):
    cleaned = re.sub(r"[^a-zA-Z0-9']+", " ", sentence).lower().strip()
    words = cleaned.split()
    words = [word.strip("'") for word in words if word.strip("'") != ""]
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

    # transformed_sentence = re.sub(r"[^a-zA-Z0-9']+", " ", sentence).lower()
    # arr = re.sub(r"\s+", " ", transformed_sentence).split(" ")
    # print(arr)
    # transformed_arr = sorted([i.strip("'") for i in arr if i.strip("'") != ""])
    # print(transformed_arr)
    # counts = {}
    # for word in transformed_arr:
    #     counts[word] = counts.get(word, 0) + 1

    # print(counts)

    # return counts
