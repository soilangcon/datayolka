#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rows = []
    for each_row in range(a.shape[0]):
        rows.append(a[each_row, :])
    return rows

def get_columns(a):
    cols = []
    for each_col in range(a.shape[1]):
        cols.append(a[:, each_col])
    return cols

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
