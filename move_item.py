def move_item(lst, index, direction):
    if direction == "left":
        new_index = index - 1
        while new_index >= 0 and lst[new_index] == 0:
            new_index -=1
        if new_index >= 0:
            lst[new_index], lst[index] = lst[index], 0
    if direction == "right":
        new_index = index + 1
        while new_index < len(lst) and lst[new_index] == 0:
            new_index += 1
        if new_index == len(lst):
            new_index = len(lst) - 1
        elif lst[new_index] != 0:
            new_index -=1
        lst[new_index], lst[index] = lst[index], 0
    return lst
def main():
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print( move_item(original_list, 3,  "left") )
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print( move_item(original_list, 3, "right") )
    original_list = ["a", 0, 0, "b", "c", 0, 0]
    print( move_item(original_list, 4, "right") )
main()