def build_car(w):
    c = '.-----------' + ('-' * w) +'.\n'
    c += '| ### ||  ###' + ('#' * w) +'\\\n'
    c += '| ### ||  ####' + ('#' * w) +'\\.\n'
    c += 'D     ||  ' + (' ' * w) +'<>    |------+\n'
    c += '|  ______      ' + (' ' * w) +'/______ |\n'
    c += ' \/ /..\ \_____' + ('_' * w) +'/ /..\ \|\n'
    c += '    \__/         ' + (' ' * w) +'\__/'
    return c

width = 5
car = build_car(width)
print(car, end="")