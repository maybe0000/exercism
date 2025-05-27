def encode(plain_text):
    cleaned = "".join([c for c in plain_text if c.isalnum()]).lower()

    def transform(chars):
        return "".join(
            chr(ord(x) + 25 - 2 * (ord(x) - 97)) if x.isalpha() else x
            # format
            for x in chars
        )

    return " ".join(transform(cleaned[i : i + 5]) for i in range(0, len(cleaned), 5))


def decode(ciphered_text):
    return encode(ciphered_text).replace(" ", "")
