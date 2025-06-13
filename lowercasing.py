def lowercase_items(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            words[i][j] = words[i][j].lower()
    return words 
