#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    words = dir(hidden_4)
    for i in words:
        if i[0] != '_' and i[1] != '_':
            print("{}".format(i))        
