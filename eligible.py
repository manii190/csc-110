def validate_age(age):
    if age.isnumeric():
        age_int = int(age)
        return 0 <= age_int <= 110
    return False
def check_eligibility(age):
    if age >= 18:
        return True
    else :
        return False

print( validate_age("20") ) # True
print( validate_age("20.5") ) # False
print( validate_age("20a") ) # False
print( validate_age("300") ) # False
print( check_eligibility(20) ) # True
print( check_eligibility(15) ) # False