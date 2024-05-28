#!/usr/bin/env python3

def extract_numbers(s):
    s = s.split()
    outlist = []
    for element in s:
        try:
            isint = int(element)
            outlist.append(isint)
        except:
            try:
                isfloat = float(element)
                outlist.append(isfloat)
            except:
                continue
    return outlist

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
