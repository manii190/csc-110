
def read_file(filename):
  new_list = []
  file = open(filename, "r")
  for line in file:
    line_parts = line.strip().split(",")
    for p in line_parts:
      new_list.append(p)
  return new_list

def count_names(name_list):
    my_counts = {}
    for item in name_list:
        item = item.strip()
        try:
            float(item)
        except ValueError:
            my_counts[item] = my_counts.get(item, 0) + 1
    return my_counts


def find_name(name_counts, name):
    if name in name_counts:
        message = f"The name {name} occurs {name_counts[name]} times."
        return message
    else:
        message = f"{name} not found."
        return message
    
def get_most_common_name(name_counts):
    most_common_name = None
    most_common_count = 0
    
    for name, count in name_counts.items():
        if count > most_common_count:
            most_common_name = name
            most_common_count = count
    
    return f"The name {most_common_name} occurs {most_common_count} times."


my_list = read_file("names_and_numbers.txt")
my_counts = count_names(my_list)
print( my_counts )

my_list = read_file("names_and_numbers.txt")
my_counts = count_names(my_list)
print( get_most_common_name(my_counts) )

my_list = read_file("names_and_numbers.txt")
my_counts = count_names(my_list)
print( find_name(my_counts, "Adriana") )