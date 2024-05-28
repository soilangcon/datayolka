#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    return a[np.sum(a[:, 0:int(a.shape[1]/2)],axis=1)>np.sum(a[:, int(a.shape[1]/2):],axis=1)]

def main():
    pass

if __name__ == "__main__":
    main()
