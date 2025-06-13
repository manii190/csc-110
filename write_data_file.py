def write_csv(dict,filename):
    file=open(filename,'w')
    for key,value in dict.items():
        file.write(str(key))
        file.write(',')
        index=0
        while index in range(len(value)):
            if index<(len(value)-1):
                file.write(str(value[index]))
                file.write(',')
            else:
                file.write(str(value[index]))
            index+=1
        file.write('\n')
    file.close()
