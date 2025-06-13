"""

def print_some_words(file_name,n):
    f=open(file_name)
    for lines in f:
        words=lines.strip().split()
        for w in words :
            w=w.strip(".,;?")
            if len(w)>=n:
                print(w)
    f.close()


print_some_words("poem.txt",6)"""
"""
def print_keys(d):
    for keys in d:
        print(keys)

def even(d):
    for keys in d:
        if keys%2==0:
            print(keys)

def keys_dicts(d,words):
    for w in words:
        if w in d:
            print(True)
        else:
            print(False)
"""
"""
def key_of_max_value(adict):
    max_key=""
    max_value=0
    for key in adict:
        if adict[key]>max_value:
            max_value=adict[key]
            max_key=key
    return max_key
print(key_of_max_value({"hello" : 34, "sunny" : 51, "the" : 82, "street" : 13}))
"""
"""
def mutiply_grid(grid,offset):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j]*=offset
    return grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

offset = 2
print(mutiply_grid(grid,offset))
"""
"""
def column2list(grid,n):
    new_list=[]
    for i in range(len(grid)):
        if n < len(grid):
            new_list.append(grid[i][n])
    return new_list
"""
"""
def grid_is_square(lists):
    total_list=len(lists)
    for i in range(len(lists)):
        if len(list[i])==total_list:
            print(True)
        else:
            print(False)
"""
"""
def max_consec_sum(number,n):
    sum=0
    for i in range(n):
        sum+=number[i]
    return sum
#def main():
#   print( max_consec_sum([10,2,-3,4,3],3))
#main()

def cv_match(sentence,pattern):
    words=sentence.strip().split()
    new_list=[]
    for word  in words:
        new_string=""
        if len(word)==len(pattern):
            for w in word:
                if w not in "aeiou":
                    new_string+= 'c'
                else:
                    new_string+= 'v'
        if new_string==pattern:
            new_list.append(word)
    return new_list
print(cv_match("Tim has a pet rat named Nip", "cvc"))

"""
"""
def sum_csv_string(csv_string):
    sum=0
    numbers=csv_string.split(',')
    for n in numbers:
        sum+=int(n)
    return sum
print(sum_csv_string("11,22,33"))
"""
"""
def list2dict(lis2d):
    new_dict={}
    for list in lis2d:
        new_dict[list[0]]=list[1:]
    return new_dict
x2 = [
    ['aa', 'bb'],
    ['cc', 'dd'],
    ['ee', 'ff'],
    ['gg', 'hh'],
    ['kk', 'll']
]
print(list2dict(x2))
"""
"""
def invert_dict(d):
    inverted = {}
    
    for key, value in d.items():
        inverted[value] = key
    return inverted
"""
"""
def numbers():
    n=input("enter the number")
    if n.isnumeric():
        int_n=int(n)
        for i in range(int_n+1):
            print(i)
    else:
        input("enter the number")
print(numbers())
"""
def concat_elements(slist, startpos, stoppos):
    if startpos > stoppos:
        return ""
    if startpos < 0:
        startpos = 0
    if stoppos >= len(slist):
        stoppos = len(slist) - 1
    result = ""
    for i in range(startpos, stoppos + 1):
        result+=slist[i]
    return result

def concat_elements(slist, startpos, stoppos):
    startpos = max(0, startpos)
    stoppos = min(len(slist) - 1, stoppos)
    if startpos > stoppos:
        return ""
    return ''.join(slist[startpos:stoppos + 1])

def shuffle_dic(somedict):
    sorted_keys=[]
    sorted_values=[]
    for keys,values in somedict.items():
        sorted_keys.append(keys)
        sorted_values.append(values)
    return sorted(sorted_keys),sorted(sorted_values)


