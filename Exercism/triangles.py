def equilateral(sides):
    return valid_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return valid_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return valid_triangle(sides) and len(set(sides)) == 3