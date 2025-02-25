def checkIfTriangle(a,b,c):
    if a + b < c or b + c < a or a + c < b or a == 0 or b == 0 or c == 0:
        return False
    return True

def equilateral(sides):
    a, b, c = sides
    if not checkIfTriangle(a,b,c):
        return False
    if a == b == c:
        return True
    return False


def isosceles(sides):
    a, b, c = sides
    if not checkIfTriangle(a,b,c):
        return False
    if a == b or b == c or a == c:
        return True
    return False


def scalene(sides):
    a, b, c = sides
    if not checkIfTriangle(a,b,c):
        return False
    if not equilateral(sides) and not isosceles(sides):
        return True
    return False
