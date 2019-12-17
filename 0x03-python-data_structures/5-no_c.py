#!/usr/bin/python3
def no_c(my_string):
    count = 0
    for i in my_string:
        count += 1
        if i == 'c' or i == 'C':
            new_string = my_string[:count - 1] + my_string[count:]
            my_string = new_string
            count -=1
    return (new_string)
