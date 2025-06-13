def get_elements(d, n):
    result = [
        value for key, value in d.items()
        if key[0].isupper() or key[-1].isupper() or value >= n
    ]
    return result

