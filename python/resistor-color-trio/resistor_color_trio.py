def label(colors):
    res_value = ''
    add_on = ''
    nulls = ''
    k = 0
    for index in range(3):
        if index < 2:
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
    
    # 35            ohms
    # 350           ohms
    # 3500        3.5 kiloohms 
    # 35000       35 kiloohms
    # 350 000     350 kiloohms
    # 3 500 000   35 megaohms
    # 35 000 000  350 megaohms
    # 350 000 000 350 megaohms
    # 3 500 000 000 3500 megaohms
    # 35 000 000 000  35 gigaohms