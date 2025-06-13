def add_up_to(n):
    result = 0
    value=1
    while value <= n:
        result=result + value
        value += 1
    return result
    
def main():
        print(add_up_to(5))
        print(add_up_to(10))
main()
