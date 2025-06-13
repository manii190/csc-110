def read_csv(file_name):
    dict={}
    f=open(file_name,"r")
    for line in f:
        item=line.strip().split(",")
        key=item[0]
        value=[]
        for i in range(1,len(item)):
            if item[i].isnumeric() == True or str(item[i][0]) in '0123456789':
                values=float(item[i])
            else:
                values=item[i]
            value.append(values)
        dict[key] = value
    f.close()
    return dict

