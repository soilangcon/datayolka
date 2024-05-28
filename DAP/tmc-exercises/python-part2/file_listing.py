#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    outlist = []
    with open(filename, 'r') as file:
        for line in file: 
            pattern = r'\s+(\d+)\s+([A-Z][a-z]+)\s+(\d+)\s+(\d+):(\d+)\s+(\S+)'
            matched = re.findall(pattern, line.strip())[0]
            size, month, day, hour, minute, filename = matched
            outlist.append((int(size), month, int(day), int(hour), int(minute), filename))
    return outlist

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
