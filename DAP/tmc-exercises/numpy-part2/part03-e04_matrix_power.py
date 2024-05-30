from functools import reduce
import numpy as np

def matrix_power(a, n):
    """
    if n >= 0:
        return reduce(lambda m1, m2: m1 @ m2, (a for _ in range(n))) if n> 0 else np.eye(a.shape[0])
    else:
        return reduce(lambda m1, m2: m1 @ m2, (np.linalg.inv(a) for _ in range(-n)))
    """
    return reduce(lambda m1, m2: m1 @ m2, (np.linalg.inv(a) if n < 0 else a for _ in range(abs(n))), np.eye(a.shape[0]))
 
def main():
    return
 
if __name__ == "__main__":
    main()
 
