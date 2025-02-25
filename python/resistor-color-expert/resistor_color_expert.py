def label(colors):
    res_value = ''
    add_on = ''
    nulls = ''
    k = 0
    for index in range(len(colors)):
        if index < len(colors)-1:
            res_value += color_dict()[colors[index]]
        else:
            nulls += int(color_dict()[colors[index]])*'0'
    if nulls=='' or int(res_value+nulls)//1000 == 0:
        res_value = int(res_value + nulls)
        add_on = ' ohms'
        return str(res_value) + add_on
    if 1 <= int(res_value+nulls)//1000 < 1000:
        add_on = ' kiloohms'
    elif int(res_value+nulls)//1000 < 9999999:
        k = 3
        add_on = ' megaohms'
    elif int(res_value+nulls)//1000 >= 9999999:
        k = 6
        add_on = ' gigaohms'
    res_value = int(res_value+nulls)/(1000*10**k)
    return str(int(res_value) if res_value.is_integer() else res_value) + add_on

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
    
def resistor_dict():
    return {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }
def resistor_label(colors):
    if len(colors) == 1:
        return color_dict()[colors[0]] + ' ohms'
    return label(colors[:-1]) + ' ±' + resistor_dict()[colors[-1]]
    