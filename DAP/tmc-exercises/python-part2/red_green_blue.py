#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    outlist = []
    with open(filename, 'r') as file:
        for line in file: 
            pattern = r'(\d+)\s+(\d+)\s+(\d+)\s+(\w.*)'
            matched = re.findall(pattern, line.strip())
            if len(matched) != 0:
                red, green, blue, colorname = matched[0]
                outlist.append("\t".join([red, green, blue, colorname]))
    return outlist


def main():
    print(red_green_blue(filename="part02-e03_red_green_blue/src/rgb.txt"))

if __name__ == "__main__":
    main()
