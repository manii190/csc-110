def all_mappings(D):
    dictonary=[]
    for key,values in D.items():
        for i in range(len(values)):
            value=values[i]
            dictonary.append((key,value))
    return dictonary
