import re


def abbreviate(words):
    cleaned = re.split(r"[\s_-]+", words)
    return "".join(word[0] for word in cleaned if word and word[0].isalpha()).upper()
