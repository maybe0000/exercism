def color_code(color):
    color_dict = dict(list(zip(colors(), range(10))))
    return color_dict[color]

def colors():
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
