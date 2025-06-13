def max_list(numbers):
  max = None
  for i in range(len(numbers)):
    if max == None or numbers[i] > max:
      max = numbers[i]
  return max

def nested_max(lists):
  max = None
  for i in range(len(lists)):
    max_of_sublist = max_list(lists[i])
    if max == None or  max_of_sublist> max:
      max = max_of_sublist
  return max

def main():
  assert nested_max([[], []]) == None
  assert nested_max([[1, 2, 3, 2, 1],
                     [2, 3, 2, 1, 5],
                     [0, 1]]) == 5
  print("Passed all tests")
main()