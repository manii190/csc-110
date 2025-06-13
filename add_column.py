def read_ids(file_name):
    id_dict = {}
    f = open(file_name, 'r')
    for line in f:
        parts = line.strip().split(',')
        id = parts[0]
        name = parts[1]
        id_dict[id] = name
    f.close()
    return id_dict

def add_name_column(txt_file, id_dict):
    output_file = "output_" + txt_file
    file = open(txt_file, 'r')
    output = open(output_file, 'w')
    for line in file:
        parts = line.strip().split('\t')
        id = parts[0]
        city = parts[1]
        if id in id_dict:
            name = id_dict[id]
        else:
            name = "Unknown"
        output.write(id + ',' + name + ',' + city + '\n')
    file.close()
    output.close()
id_names = read_ids("ids_and_names.csv")
print(id_names)