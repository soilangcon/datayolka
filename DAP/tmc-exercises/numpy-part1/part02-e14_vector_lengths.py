import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
    a = np.array([[ 72, -53, 17, 92, -33],
    [ 95, 3, -91, -79, -64],
    [-13, -30, -12, 40, -42],
    [ 93, -61, -13, 74, -12]])
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
