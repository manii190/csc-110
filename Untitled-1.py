
def rectangle_area(base,height):
    return (base*height)
def triangle_area(a,b,c):
    s=(a+b+c)/2
    return((s*(s-a)*(s-b)*(s-c))**0.5)
def trapezoid_area(b1.b2.h):
    return(0.5*(b1+b2)*h)
def circle_area(r)
    return(3.145*r**2)
def calculate_area(shape, a1, a2, a3):
    if shape == 'rectangle':
        area = rectangle_area(a1, a2)
        message = "The area of the {} is{}".format(shape, area)
        return message
    
    else if shape == 'triangle':
        area = triangle_area(a1, a2, a3)
        message = "The area of the {} is {}".format(shape, area)
        return message
    
    else if shape == 'trapezoid':
    area = trapezoid_area(a1, a2, a3)
    message = "The area of the {} is {}".format(shape, area)
    return message
    
    else if shape == 'circle':
    area = circle_area(a1)
    message = "The area of the {} is {}".format(shape, area)