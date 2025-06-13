def concatenate(words):
    result = ""
    index = 0
    while index < len(words):
        result += words[index]
        index += 1  # Increment the index
        if index < len(words):
            result += " "
    return result
def main():
    value = concatenate([])
    assert value == "", \
        f"expected return value was an empty string, but function returned {value}" 

    value = concatenate(["", "", ""])
    assert value == "  ", \
        f"expected return value was an \"  \", but function returned {value}" 

    value = concatenate(["Hi", "there"])
    assert value == "Hi there", \
        f"expected return value was an \"Hi There\", but function returned {value}" 

print("All tests passed.")

main()