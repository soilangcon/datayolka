#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    x, y =  data[:, 0], data[:, 2]
    return scipy.stats.pearsonr(x, y)[0]

def correlations():
    # return np.corrcoef(load(), rowvar=False)
    return np.corrcoef(load().transpose(), rowvar=True)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
