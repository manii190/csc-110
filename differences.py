def differences(set_1, set_2):
    return len(set_1 ^ set_2)

def has_duplicate(lst):
    return len(lst) != len(set(lst))

