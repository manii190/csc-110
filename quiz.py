import random

def create_two_d_list(width, length):
  """
  This function creates a 2D list of random integers using nested loops.

  Args:
      width: The length of each sublist.
      length: The number of sublists in the main list.

  Returns:
      A 2D list of random integers between 0 and 100.
  """
  random.seed(123)  # Set the random seed for consistency
  two_d_list = []
  for _ in range(length):
    sublist = []
    for _ in range(width):
      sublist.append(random.randint(0, 100))
    two_d_list.append(sublist)
  return two_d_list
# Examples
my_two_d_list = create_two_d_list(5, 3)
print(my_two_d_list)

my_two_d_list = create_two_d_list(3, 5)

print(my_two_d_list)
two_d_list = []
    for _ in range (l):
        sublist = []
        for _ in range (w):
            sublist.append(random.randint(0, 100))
        two_d_list.append(sublist)
    return two_d_list