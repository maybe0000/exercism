christmas_dict = {
    "first": "and a Partridge in a Pear Tree.",
    "second": "two Turtle Doves",
    "third": "three French Hens",
    "fourth": "four Calling Birds",
    "fifth": "five Gold Rings",
    "sixth": "six Geese-a-Laying",
    "seventh": "seven Swans-a-Swimming",
    "eighth": "eight Maids-a-Milking",
    "ninth": "nine Ladies Dancing",
    "tenth": "ten Lords-a-Leaping",
    "eleventh": "eleven Pipers Piping",
    "twelfth": "twelve Drummers Drumming",
}


def recite(start_verse, end_verse):
    if start_verse > end_verse or start_verse < 1 or end_verse < 1:
        return [""]
    prefix = "On the "
    postfix = " day of Christmas my true love gave to me: "
    tmp = ""
    gifts = []
    for i in range(start_verse, end_verse + 1):
        tmp = (
            prefix
            + list(christmas_dict.keys())[i - 1]
            + postfix
            + ", ".join(reversed(list(christmas_dict.values())[:i]))
        )
        if i == 1:
            tmp = tmp.replace("and a Partridge", "a Partridge")
        gifts.append(tmp.strip())
    # print(gifts)
    return gifts
