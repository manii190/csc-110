def max3(x, y, z):
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    if z >= x and z >= y :
        return z
def main():
    print( max3(1, 1, 1) ) # 1
    print( max3(1, 2, 1) ) # 2
    print( max3(-1, -1, 0) ) # 0
    print( max3(100, 0, 0) ) # 100
    print( max3(19, 19, 0) ) # 19
    print( max3(2, 0, 2) ) # 2
    print( max3(-100, 0, 0) ) # 0
main()
