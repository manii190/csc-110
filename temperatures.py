def celsius_to_fahrenheit(celsius):
    return round(celsius*1.8+32,2)
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit-32)*5/9,2)
def main():
    print( celsius_to_fahrenheit(15) ) # 59.0
    print( celsius_to_fahrenheit(25) ) # 77.0
    print( celsius_to_fahrenheit(38) ) # 100.4
    print( fahrenheit_to_celsius(100) ) # 37.78
    print( fahrenheit_to_celsius(115) ) # 46.11
    print( fahrenheit_to_celsius(75) ) # 23.89
main()