def rectangle_area(base, height):
    return (base * height)

def triangle_area(a, b, c):
    s = ((a+b+c) / 2)
    return(s * (s-a) * (s-b) * (s-c)) ** 0.5

def trapezoid_area(b1, b2, h):
    return (1/2 * (b1 + b2) * h)

def circle_area(radius):
    a=  3.1415 * radius ** 2
    return round(a, 2)

def calculate_area(shape, n1, n2, n3):
    if shape == 'rectangle':
        area = rectangle_area(n1, n2)
        message = "The area of the {} is{}".format(shape, area)
        return message
    
    elif shape == 'triangle':
        area = triangle_area(n1, n2, n3)
        message = "The area of the {} is {}".format(shape, area)
        return message
    
    elif shape == 'trapezoid':
        area = trapezoid_area(n1, n2, n3)
        message = "The area of the {} is {}".format(shape, area)
        return message
    
    elif shape == 'circle':
        area = circle_area(n1)
        message = "The area of the {} is {}".format(shape, area)
        return message