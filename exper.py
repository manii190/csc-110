
def move_item(lst, index, direction):
    if direction == "left":
        new_index = index - 1
        # Move left, skipping zeros
        while new_index >= 0 and lst[new_index] == 0:
            new_index -= 1
        # Perform the swap only if a valid position is found
        if new_index >= 0:
            lst[new_index], lst[index] = lst[index], 0

    elif direction == "right":
        new_index = index + 1
        # Move right, skipping zeros
        while new_index < len(lst) and lst[new_index] == 0:
            new_index += 1
        # If no non-zero found, move to the farthest right (last zero)
        if new_index == len(lst):  # Means we moved past all items
            new_index = len(lst) - 1
        # Perform the swap
        lst[new_index], lst[index] = lst[index], 0

    return lst

def main():
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print(move_item(original_list, 3, "left"))  # Expected: ['b', 0, 0, 0, 'c', 0, 0]
    
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print(move_item(original_list, 3, "right"))  # Expected: ['a', 0, 0, 0, 'b', 0, 0]
    
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print(move_item(original_list, 4, "right"))  # Expected: ['a', 0, 0, 0, 0, 0, 'b']

main()

