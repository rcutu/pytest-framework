
def add_dots(string):
    new_string = ''
    for i in range(0, len(string)-1):
        new_string = new_string + string[i] + '.'
    return new_string+string[len(string)-1]


def remove_dots(string):
    new_string = ''
    for c in string:
        if c != '.':
            new_string += c
    return new_string
