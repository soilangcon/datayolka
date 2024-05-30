import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    if a1 == a2:
        if b1 == b2:
            return (float('inf'), float('inf')), False # Lines are identical
        else:
            return (float('inf'), float('inf')), False # Lines are parallel
    A = np.array([[-a1, 1], [-a2, 1]])
    b = np.array([b1, b2])
    solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    x, y = solution
    exact = residuals.size == 0 or np.isclose(residuals, 0).all()
    return (x, y), exact

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
