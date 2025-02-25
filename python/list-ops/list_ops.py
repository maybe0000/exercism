def append(list1, list2):
    return list1 + list2

def concat(lists):
    concatenated_list = []
    for list in lists:
        concatenated_list += list
    return concatenated_list

def filter(function, list):
    filtered_list = []
    for el in list:
        if function(el):
            filtered_list += [el]
    return filtered_list

def length(list):
    counter = 0
    for el in list:
        counter += 1
    return counter

def map(function, list):
    mapped_list = []
    for el in list:
        mapped_list += [function(el)]
    return mapped_list

def foldl(function, list, initial):
    reduction = initial
    for el in list:
        reduction = function(reduction, el)
    return reduction

def foldr(function, list, initial):
    reduction = initial
    for el in list[::-1]:
        reduction = function(reduction, el)
    return reduction

def reverse(list):
    reversed_list = []
    for el in list[::-1]:
        reversed_list += [el]
    return reversed_list
