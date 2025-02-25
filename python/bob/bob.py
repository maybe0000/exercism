def response(hey_bob: str):
    stripped_question = hey_bob.strip()
    if len(stripped_question) == 0:
        return "Fine. Be that way!"
    if stripped_question[-1] == '?':
        if all(c.isupper() if c.isalpha() else True for c in stripped_question) and any(c.isalpha() for c in stripped_question):
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if all(c.isupper() if c.isalpha() else True for c in stripped_question) and any(c.isalpha() for c in stripped_question):
        return "Whoa, chill out!"
    return "Whatever."
