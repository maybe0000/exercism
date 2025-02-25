def value(colors):
    res_value = ''
    for index in range(2):
        #print(index, colors, colors[index], color_dict()[colors[index]])
        res_value += color_dict()[colors[index]]
    return int(res_value)

def color_dict():
    return {
            "black": '0',
            "brown": '1',
            "red": '2',
            "orange": '3',
            "yellow": '4',
            "green": '5',
            "blue": '6',
            "violet": '7',
            "grey": '8',
            "white": '9'
    }