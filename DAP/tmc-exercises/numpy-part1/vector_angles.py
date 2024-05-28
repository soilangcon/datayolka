#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    return np.degrees(np.arccos(np.clip(np.sum(X*Y, axis=1)/(np.linalg.norm(X, axis=1) * np.linalg.norm(Y, axis=1)), -1.0, 1.0)))


def main():
    X = np.array([[1, 2, 3], [4, 5, 6]])
    Y = np.array([[7, 8, 9], [10, 11, 12]])
    vector_angles(X, Y)

if __name__ == "__main__":
    main()
