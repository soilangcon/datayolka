#!/usr/bin/env python3

def interleave(*lists):
    outlist = []
    for tuple in list(zip(*lists)):
        outlist.extend(tuple)
    return outlist

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
