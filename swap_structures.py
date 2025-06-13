def swap(d, s):
    keys_to_swap = [key for key in d if key in s]
    for key in keys_to_swap:
        value = d[key]
        d[value] = key
        del d[key]