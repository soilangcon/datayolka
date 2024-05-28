#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    rows = []
    for each_row in range(a.shape[0]):
        rows.append(a[each_row, :].reshape(1, -1))
    return rows

def get_column_vectors(a):
    cols = []
    for each_col in range(a.shape[1]):
        cols.append(a[:, each_col].reshape(-1, 1))
    return cols

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
